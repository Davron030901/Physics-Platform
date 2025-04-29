# fiziktest/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Question, Choice, UserAnswer, TestSession
import random

# fiziktest/views.py (test_list funksiyasi)
def test_list(request):
    """Test kategoriyalarini ko'rsatadigan sahifa"""
    topics = Question.TOPICS
    
    # Statistikani olish
    topic_stats = {}
    if request.user.is_authenticated:
        for topic_key, topic_name in topics:
            questions_count = Question.objects.filter(topic=topic_key).count()
            correct_answers = UserAnswer.objects.filter(
                user=request.user,
                question__topic=topic_key,
                is_correct=True
            ).count()
            
            if questions_count > 0:
                percentage = int((correct_answers / questions_count) * 100)
            else:
                percentage = 0
                
            topic_stats[topic_key] = {
                'name': topic_name,
                'questions_count': questions_count,
                'correct_answers': correct_answers,
                'percentage': percentage
            }
    
    context = {
        'topics': topics,
        'topic_stats': topic_stats
    }
    
    return render(request, 'fiziktest/test_list.html', context)
def start_test(request, topic=None):
    """Test boshlash"""
    # Testlar mavjudligini tekshirish
    questions = Question.objects.all()
    if topic:
        questions = questions.filter(topic=topic)
    
    if not questions.exists():
        messages.warning(request, "Hozircha test savollari mavjud emas.")
        return redirect('test_list')
    
    # Yangi test sessiyasi yaratish
    if request.user.is_authenticated:
        # Oldingi tugallanmagan testni tugallangan deb belgilash
        TestSession.objects.filter(user=request.user, finished_at=None).update(finished_at=timezone.now())
        
        # Savollarni tasodifiy tartibda olish (maksimum 10 ta)
        questions = list(questions.order_by('?')[:10])
        
        session = TestSession.objects.create(
            user=request.user,
            total_questions=len(questions)
        )
        for question in questions:
            session.questions.add(question)
        # Birinchi savolga o'tish
        return redirect('question', session_id=session.id, question_index=0)
    else:
        # Login qilmagan foydalanuvchilar uchun demo test
        questions = list(questions.order_by('?')[:5])
        return render(request, 'fiziktest/demo_test.html', {'questions': questions})

def question(request, session_id, question_index):
    """Test savollari sahifasi"""
    # Sessiyani tekshirish
    if not request.user.is_authenticated:
        messages.warning(request, "Testda qatnashish uchun tizimga kirishingiz kerak.")
        return redirect('account_login')
    
    session = get_object_or_404(TestSession, id=session_id, user=request.user)
    
    # Test tugagan bo'lsa
    if session.finished_at:
        return redirect('test_result', session_id=session.id)
    
    # Test vaqti tugagan bo'lsa (30 daqiqa)
    if (timezone.now() - session.started_at).total_seconds() > 30*60:
        session.finished_at = timezone.now()
        session.save()
        messages.info(request, "Test vaqti tugadi.")
        return redirect('test_result', session_id=session.id)
    
    # Savollar olish (kerakli tartibda)
    # Sessiya yaratilganda qo'shilgan savollarni olish uchun
    # sessionga savollari yoki test_id qo'shilishi kerak edi
    # Hozirlik uchun barcha savollardan tasodifiy olishni davom ettiramiz
    questions = list(Question.objects.all().order_by('?')[:10])
    
    # Savollar tugagan bo'lsa
    if question_index >= len(questions):
        session.finished_at = timezone.now()
        session.save()
        return redirect('test_result', session_id=session.id)
    
    current_question = questions[question_index]
    
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if not choice_id:
            messages.error(request, "Iltimos, javob variantini tanlang.")
            return render(request, 'fiziktest/question.html', {
                'session': session,
                'question': current_question,
                'question_index': question_index,
                'total_questions': len(questions),
                'time_passed': int((timezone.now() - session.started_at).total_seconds())
            })
        
        choice = get_object_or_404(Choice, id=choice_id)
        
        # Javobni saqlash
        user_answer, created = UserAnswer.objects.get_or_create(
            user=request.user,
            question=current_question,
            defaults={'choice': choice, 'is_correct': choice.is_correct}
        )
        
        if not created:
            user_answer.choice = choice
            user_answer.is_correct = choice.is_correct
            user_answer.save()
        
        # To'g'ri javob bo'lsa, ball qo'shish
        if choice.is_correct:
            session.score += current_question.points
            session.save()
        
        # Keyingi savolga o'tish
        return redirect('question', session_id=session.id, question_index=question_index+1)
    
    return render(request, 'fiziktest/question.html', {
        'session': session,
        'question': current_question,
        'question_index': question_index,
        'total_questions': len(questions),
        'time_passed': int((timezone.now() - session.started_at).total_seconds())
    })

def test_result(request, session_id):
    session = get_object_or_404(TestSession, id=session_id, user=request.user)
    
    # Foydalanuvchi bergan javoblarni olish
    user_answers = UserAnswer.objects.filter(user=request.user, question__in=session.questions.all())
    
    # To'g'ri javoblar sonini hisoblash
    correct_count = user_answers.filter(is_correct=True).count()
    
    # Test natijalari
    percentage = int(session.score / session.total_questions * 100) if session.total_questions > 0 else 0
    
    # Baho aniqlash
    grade = "Muvaffaqiyatsiz"
    if percentage >= 90:
        grade = "A'lo (5)"
    elif percentage >= 80:
        grade = "Yaxshi (4)"
    elif percentage >= 70:
        grade = "Qoniqarli (3)"
    elif percentage >= 60:
        grade = "O'rtacha (3-)"
    
    return render(request, 'fiziktest/result.html', {
        'session': session,
        'user_answers': user_answers,
        'correct_count': correct_count,
        'total_questions': session.total_questions,
        'percentage': percentage,
        'grade': grade
    })
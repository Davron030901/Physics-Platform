# loyihalar/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm, ProjectReviewForm

def loyiha_list(request):
    if request.user.is_authenticated:
        if request.user.profile.role == 'teacher':
            projects = Project.objects.filter(status='submitted')
        else:
            projects = Project.objects.filter(student=request.user)
    else:
        projects = Project.objects.filter(status='approved')
    
    return render(request, 'loyihalar/loyiha_list.html', {'projects': projects})

def loyiha_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Loyiha egasi yoki o'qituvchi bo'lmasa va loyiha tasdiqlanmagan bo'lsa, ko'rishga ruxsat yo'q
    if project.status != 'approved' and request.user != project.student and request.user.profile.role != 'teacher':
        messages.error(request, "Bu loyihani ko'rishga ruxsatingiz yo'q.")
        return redirect('loyiha_list')
    
    return render(request, 'loyihalar/loyiha_detail.html', {'project': project})

@login_required
def loyiha_create(request):
    if request.user.profile.role != 'student':
        messages.error(request, "Faqat talabalar loyiha qo'sha oladi.")
        return redirect('loyiha_list')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.student = request.user
            project.save()
            messages.success(request, "Loyiha muvaffaqiyatli qo'shildi!")
            return redirect('loyiha_list')
    else:
        form = ProjectForm()
    
    return render(request, 'loyihalar/loyiha_form.html', {'form': form, 'action': 'create'})

@login_required
def loyiha_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user != project.student:
        messages.error(request, "Siz bu loyihani o'zgartira olmaysiz!")
        return redirect('loyiha_list')
    
    if project.status != 'draft' and project.status != 'rejected':
        messages.error(request, "Topshirilgan loyihani o'zgartira olmaysiz!")
        return redirect('loyiha_detail', pk=project.pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Loyiha muvaffaqiyatli o'zgartirildi!")
            return redirect('loyiha_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'loyihalar/loyiha_form.html', {'form': form, 'project': project, 'action': 'edit'})

@login_required
def loyiha_submit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user != project.student:
        messages.error(request, "Siz bu loyihani topshira olmaysiz!")
        return redirect('loyiha_list')
    
    if project.status != 'draft' and project.status != 'rejected':
        messages.error(request, "Bu loyiha allaqachon topshirilgan!")
        return redirect('loyiha_detail', pk=project.pk)
    
    project.status = 'submitted'
    project.save()
    messages.success(request, "Loyiha muvaffaqiyatli topshirildi!")
    
    return redirect('loyiha_detail', pk=project.pk)

# loyihalar/views.py (davomi)
@login_required
def loyiha_review(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user.profile.role != 'teacher':
        messages.error(request, "Faqat o'qituvchilar loyihalarni baholay oladi!")
        return redirect('loyiha_list')
    
    if project.status != 'submitted':
        messages.error(request, "Bu loyiha baholash uchun topshirilmagan!")
        return redirect('loyiha_detail', pk=project.pk)
    
    if request.method == 'POST':
        form = ProjectReviewForm(request.POST, instance=project)
        if form.is_valid():
            reviewed_project = form.save(commit=False)
            reviewed_project.teacher = request.user
            reviewed_project.save()
            messages.success(request, "Loyiha muvaffaqiyatli baholandi!")
            return redirect('loyiha_list')
    else:
        form = ProjectReviewForm(instance=project)
    
    return render(request, 'loyihalar/loyiha_review.html', {'form': form, 'project': project})

@login_required
def loyiha_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.user != project.student and not request.user.is_staff:
        messages.error(request, "Siz bu loyihani o'chira olmaysiz!")
        return redirect('loyiha_list')
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Loyiha muvaffaqiyatli o'chirildi!")
        return redirect('loyiha_list')
    
    return render(request, 'loyihalar/loyiha_confirm_delete.html', {'project': project})
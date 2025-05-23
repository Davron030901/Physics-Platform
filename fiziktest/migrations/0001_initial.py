# Generated by Django 5.2 on 2025-04-27 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('kinematika', 'Kinematika'), ('dinamika', 'Dinamika'), ('ish_va_energiya', 'Ish va Energiya'), ('impuls', 'Impuls'), ('gravitatsiya', 'Gravitatsiya')], max_length=50, verbose_name='Mavzu')),
                ('text', models.TextField(verbose_name='Savol')),
                ('time_limit', models.IntegerField(default=180, verbose_name='Vaqt chegarasi (sekund)')),
                ('points', models.IntegerField(default=1, verbose_name='Ball')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Test savoli',
                'verbose_name_plural': 'Test savollari',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Variant')),
                ('is_correct', models.BooleanField(default=False, verbose_name="To'g'ri javob")),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='fiziktest.question', verbose_name='Savol')),
            ],
            options={
                'verbose_name': 'Javob varianti',
                'verbose_name_plural': 'Javob variantlari',
            },
        ),
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='Ball')),
                ('total_questions', models.IntegerField(default=0, verbose_name='Savollar soni')),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_sessions', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Test sessiyasi',
                'verbose_name_plural': 'Test sessiyalari',
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, verbose_name="To'g'ri javob")),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiziktest.choice', verbose_name='Tanlangan javob')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiziktest.question', verbose_name='Savol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_answers', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi javobi',
                'verbose_name_plural': 'Foydalanuvchi javoblari',
                'unique_together': {('user', 'question')},
            },
        ),
    ]

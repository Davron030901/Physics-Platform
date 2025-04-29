# users/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = [
        ('teacher', "O'qituvchi"),
        ('student', "O'quvchi"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    bio = models.TextField(blank=True, verbose_name="Qisqacha ma'lumot")
    image = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="Rasm")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student', verbose_name="Rol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Foydalanuvchi profili"
        verbose_name_plural = "Foydalanuvchi profillari"

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"

    def get_avatar(self):
        if self.image:
            return self.image.url
        return '/static/images/default_user.png'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Yangi foydalanuvchi yaratilganda profil yaratish"""
    if created:
        Profile.objects.create(user=instance, full_name=instance.get_full_name() or instance.username)
    else:
        instance.profile.save()
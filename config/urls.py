# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseForbidden

# Admin paneliga kirish huquqini tekshirish
def admin_check(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden("<h1>Kirish taqiqlangan</h1>")
        return view_func(request, *args, **kwargs)
    return wrapper

admin.site.site_header = 'Fizika ta\'lim platformasi'
admin.site.site_title = 'Fizika admin'
admin.site.index_title = 'Boshqaruv paneli'
admin.site.site_url = '/'

# Barcha admin view larni himoyalash
admin.site.login = admin_check(admin.site.login)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(f'{settings.ADMIN_URL}', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('maruza/', include('maruza.urls')),
    path('amaliy/', include('amaliy.urls')),
    path('labaratoriya/', include('labaratoriya.urls')),
    path('fiziktest/', include('fiziktest.urls')),
    path('krossvord/', include('krossvord.urls')),
    path('loyihalar/', include('loyihalar.urls')),
    path('simulation-games/', include('simulation_games.urls')),
    path('sonmetodi/', include('sonmetodi.urls')),
    path('suzmetodi/', include('suzmetodi.urls')),
    path('videos/', include('videos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
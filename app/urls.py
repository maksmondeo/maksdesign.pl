from django.urls import path
from django.conf.urls import handler404
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

def custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_page_not_found_view

urlpatterns = [
    path('', views.index, name='index'),
    path('polityka-prywatnosci', views.polityka, name='polityka'),
    path('.well-known/discord', views.discord_verification),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
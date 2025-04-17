from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from .models import Project
from django.http import HttpResponse

import environ
env = environ.Env()
environ.Env.read_env()

def index(request):
    projects = Project.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_message = f'Wiadomość od: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}'
            send_mail(
                f'[FORM] {name}: {subject}',
                email_message,
                settings.EMAIL_HOST_USER,
                ['kontakt@maksdesign.pl'],
                fail_silently=False,
            )
            success_message = "Wiadomość została przesłana"
            return render(request, 'index.html', {'form': form, 'success_message': success_message, 'projects': projects})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form, 'projects': projects})

def polityka(request):
    return render(request, 'polityka.html')

def kontakt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            email_message = f'Wiadomość od: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}'
            send_mail(
                f'[FORM] {name}',
                email_message,
                settings.EMAIL_HOST_USER,
                ['kontakt@maksdesign.pl'],
                fail_silently=False,
            )
            success_message = "Wiadomość została przesłana"
            return render(request, 'kontakt.html', {'form': form, 'success_message': success_message})
    else:
        form = ContactForm()
    return render(request, 'kontakt.html', {'form': form})

def discord_verification(request):
    return HttpResponse(env('DISCORD_KEY'), content_type="text/plain")
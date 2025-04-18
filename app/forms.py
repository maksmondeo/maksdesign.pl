from django import forms
from .models import Project
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    SUBJECT_CHOICES = [
        ("Grafika", "Grafiki"),
        ("Strona Internetowa", "Strony internetowe"),
        ("Inne", "Inne"),
    ]
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Imię"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    phone = forms.CharField(
        max_length=15, widget=forms.TextInput(attrs={"placeholder": "Telefon"})
    )
    subject = forms.ChoiceField(
        choices=[("", "Wybierz temat wiadomości")] + SUBJECT_CHOICES,
        widget=forms.Select(),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "np. Co chciałbyś aby znajdowało się na twojej stronie/grafice?"
            }
        )
    )
    captcha = ReCaptchaField()


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "image"]

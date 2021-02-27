from django.contrib.auth import get_user_model
from django import forms

from apps.users.utils import send_activation_mail

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'password', 'password_confirmation']

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует!')
        return email

    def save(self, commit=False):
        user = User.objects.create(**self.cleaned_data)
        # Письмо с активацией
        send_activation_mail(user)
        return user

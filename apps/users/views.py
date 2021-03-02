from django.views.generic import CreateView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic.base import View
from django.urls import reverse_lazy

from apps.users.forms import RegistrationForm


User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('successful-registration')


class SuccessfulRegistrationView(View):
    def get(self, request):
        return render(request, 'users/successful_registration.html')


class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'users/activation.html')


class SigninView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    pk_url_kwarg = 'email'



class ForgotPassword():
    pass



class ChangePassword():
    pass

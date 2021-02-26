from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic.base import View


class IndexPage(TemplateView):
    template_name = 'users/index.html'

User = get_user_model()

class RegistrationView(CreateView):
    pass


class SuccessfulRegistrationView(View):
    pass

class ActivationView(View):
    pass


class SigninView(LoginView):
    pass


class ForgotPassword():
    pass

class ChangePassword():
    pass

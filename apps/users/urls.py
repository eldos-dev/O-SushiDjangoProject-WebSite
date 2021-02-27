from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.users.views import *


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('accounts/registration/', RegistrationView.as_view(), name='registration'),
    path('accounts/successful-registration/', SuccessfulRegistrationView.as_view(), name='successful-registration'),
    path('accounts/activation/', ActivationView.as_view(), name='activation-view'),
    path('accounts/login/', SigninView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

]

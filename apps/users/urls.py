from django.urls import path

from apps.users.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]
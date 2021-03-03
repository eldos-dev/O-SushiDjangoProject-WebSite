from django.urls import path

from .views import *

urlpatterns = [
    path('admin-panel/', index_admin_panel, name='index_admin')
]
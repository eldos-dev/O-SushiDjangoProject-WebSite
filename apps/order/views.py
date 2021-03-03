from django.shortcuts import render
from django.views.generic import ListView


def index_admin_panel(request):
    return render(request, 'order/index_admin_panel.html')
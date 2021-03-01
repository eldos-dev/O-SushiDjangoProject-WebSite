from django.views.generic import ListView

from .models import Category, Product

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_products(request):
    products = Product.objects.all()[0:6]
    return {'products': products}


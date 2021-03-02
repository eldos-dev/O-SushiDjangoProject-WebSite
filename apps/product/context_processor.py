from django.views.generic import ListView

from .models import Category, Product

def get_categories(request):
    categories = Category.objects.all()
    categories_5 = Category.objects.all()[0:5]
    return {'categories': categories, 'categories_5': categories_5}

def get_products(request):
    products = Product.objects.all()[0:6]
    products_4 = Product.objects.all()[0:4]
    return {'products': products, 'products_4': products_4}


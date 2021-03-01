from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from apps.product.models import Product, Category


class IndexPage(TemplateView):
    template_name = 'users/index.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product/category_detail.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryproducts'] = Product.objects.filter(category=self.slug)
        return context



class ProductListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'
    paginate_by = 4




class ProductDeatilView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

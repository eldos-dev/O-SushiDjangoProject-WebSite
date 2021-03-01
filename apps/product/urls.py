from django.urls import path

from apps.product.views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('products/products_list/', ProductListView.as_view(), name='products-list'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]
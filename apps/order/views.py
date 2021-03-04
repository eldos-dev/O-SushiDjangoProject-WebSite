from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic.base import View

from apps.order.models import Cart, CartItem
from apps.product.models import Product

User = get_user_model()

def index_admin_panel(request):
    return render(request, 'order/index_admin_panel.html')


def order_detail(request):
    return render(request, 'order/order_detail.html')




class CartItemView(View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user.email)
        cart = Cart.objects.get(owner=user)
        cart_items = CartItem.objects.filter(cart=cart)
        context = {
            'cart': cart,
            'cart_items': cart_items,
        }
        return render(request, 'order/cart_checkout.html', context)



class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        user = User.objects.get(email=request.user.email)
        cart = Cart.objects.get(owner=user, in_order=False)
        product_info = Product.objects.get(pk=product_id)
        cart_product = CartItem.objects.create(cart=cart, product=product_info, final_price=product_info.price)
        cart_product.save()
        return redirect('cart')

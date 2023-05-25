from django.shortcuts import render, redirect, get_object_or_404
from shops.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProduct

@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProduct(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.addd(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

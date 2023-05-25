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
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('carts:cart_detail')

@require_POST
def cart_remove(request,product_id):
    cart = Cart(request.POST)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('carts: cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form']= CartAddProduct(initial={
            'quantity':item['quantity'],
            'override':True
        })
    return render(request,'carts/detail.html',{'cart':cart})
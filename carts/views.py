from django.shortcuts import render, redirect, get_object_or_404
from shops.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProduct
from coupons.forms import CouponApplyForm
from shops.recommend import Recommender


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
    recommended_products = [] 
    for item in cart:
        item['update_quantity_form'] = CartAddProduct(initial={
            'quantity':item['quantity'],
            'override':True
        })
    coupon_apply_form = CouponApplyForm()
    r = Recommender()
    cart_products = [item['product'] for item in cart]
    if(cart_products):
        recommended_posts = r.suggest_products_for(
                                 cart_products,
                                 max_result=4)
    else:
        recommended_products    
    return render(request,'carts/detail.html',{'cart':cart, 'coupon_apply_form':coupon_apply_form,'recommended_products ':recommended_products })

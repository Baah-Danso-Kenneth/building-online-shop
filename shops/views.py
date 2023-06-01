from django.shortcuts import render, get_object_or_404
from .recommend import Recommender  
from carts.forms import CartAddProduct
from .models import Category, Product

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context={'category':category,'categories':categories,'products':products}
    return render(request, 'shops/product/list.html', context)

def product_detail(request,id,slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProduct()
    r= Recommender()
    recommend_products = r.suggest_products_for([product],4)
    context={'product':product,'cart_product_form':cart_product_form,'recommend_products':recommend_products}
    return render(request,'shops/product/detail.html',context)

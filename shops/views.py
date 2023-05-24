from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(active=True)
    context={'category':category,'categories':categories,'products':products}
    return render(request, 'shops/product/list.html', context)

def product_detail(request,id,slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,'shops/product/details.html',{'product':product})
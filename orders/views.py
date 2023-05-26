from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from carts.cart import Cart


def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price = item['price'],
                                         quantity=item['quantity'])
            cart.clear()
        return render(request, 'orders/created.html',{'order':order})
    else:
        form
    context={'cart':cart,'form':form}
    return render(request, 'orders/create.html',context)



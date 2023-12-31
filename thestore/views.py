from django.shortcuts import render
from .models import *


# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'thestore/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # gets the order render to the order var or creates a new one if it doesn't exist render to the created var
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
    else:
        items = {}
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}

    context = {'items': items, 'order': order}
    return render(request, 'thestore/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # gets the order render to the order var or creates a new one if it doesn't exist render to the created var
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.order_items.all()
    else:
        items = {}
        order = {'get_cart_total': 0, 'get_cart_quantity': 0}
    context = {'items': items, 'order': order}
    return render(request, 'thestore/checkout.html', context)


import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import *
from .forms import CreateUserForm

# Create your views here.


def Register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            
            return redirect('Login')

    context = {'form': form}
    return render(request, 'store/Register.html', context)

def Login(request):
        

    context = {}
    return render(request, 'store/Login.html', context)

def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def Rod(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Rod Page.html', context)

def Reel (request):

    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Reel Page.html', context)

def Lure (request):
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Lure Page.html', context)

def Line (request):
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Line Page.html', context)

def Accessories (request):
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Accessories Page.html', context)

def Cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/Cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def increase_quantity_item(request, item_id):
    item = OrderItem.objects.get(pk=item_id)
    item.quantity = item.quantity + 1
    item.save()

    return redirect('Cart')


def decrease_quantity_item(request, item_id):
    item = OrderItem.objects.get(pk=item_id)
    item.quantity = item.quantity - 1
    item.save()

    if item.quantity <= 0:
        item.delete()

    return redirect('Cart')

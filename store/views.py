import json
import datetime
from django import forms
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import *
from .models import Vendor
from .utils import cookieCart, cartData, guestOrder
from .forms import ProductForm, UserCreationForm,UserRegisterForm, CheckoutForm, UserUpdateForm

# Create your views here.


def Register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            
            return redirect('Login')

    context = {'form': form}
    return render(request, 'store/Register.html', context)

@login_required
def Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Rod Page')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render(request, 'store/Login.html', context)

def index(request):
    context = {}
    return render(request, 'store/index.html', context)

def Vendor_Register (request):
    if request.method == "POST":
        form = UserCreationForm (request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name = user.username, created_by=user)

            return redirect("Vendor Page")
    
    else:
        form = UserCreationForm()

    return render(request, 'store/Vendor Register.html', {'form': form})

@login_required
def Vendor_Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Vendor Page')
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'store/Vendor Login.html', context)

def Vendor_Page(request):
    Vendor = request.user.vendor
    checkouts = request.user.checkout

    return render(request, 'store/Vendor Page.html', {'vendor': Vendor, 'checkout':checkouts})


def Vendor_Rod(request):
    Vendor = request.user.vendor
    products = Product.objects.all()

    return render(request, 'store/Vendor Page.html', {'vendor': Vendor, 'products': products})


def Vendor_Reel(request):
    Vendor = request.user.vendor
    products = Product.objects.all()

    return render(request, 'store/Vendor Page.html', {'vendor': Vendor, 'products': products})


def Vendor_Line(request):
    Vendor = request.user.vendor
    products = Product.objects.all()

    return render(request, 'store/Vendor Page.html', {'vendor': Vendor, 'products': products})


def Vendor_Lure(request):
    Vendor = request.user.vendor
    products = Product.objects.all()

    return render(request, 'store/Vendor Page.html', {'vendor': Vendor, 'products': products})


def Vendor_Accessories(request):
    Vendor = request.user.vendor
    products = Product.objects.all()

    return render(request, 'store/Vendor Page.html', {'vendor': Vendor, 'products': products})


@login_required
def Add_Product(request):
    Vendor = request.user.vendor
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()

            return redirect('Vendor Rod')
    else:
        form = ProductForm()
    
    return render(request, 'store/Add_Product.html', {'form': form, 'vendor':Vendor})

def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('Profile')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form}
    return render(request, 'store/Profile.html', context)

class Item(DetailView):
    model = Product
    template_name = 'store/Product.html'


class UserUpdate(UpdateView):
    model = Product
    fields = ['username', 'email']
    template_name = 'store/Update Profile.html'

    def get_success_url(self):
        return reverse_lazy('User', args=[self.object.pk])

class ItemUpdate(UpdateView):
    model = Product
    fields = ['name','price','type','brand','description','image']
    template_name = 'store/Update Product.html'
    
    def get_success_url(self):
        return reverse_lazy('Product', args=[self.object.pk])

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
            product.delete()
            return redirect('Vendor Rod')

    context = {'product':Product}
    return render(request, 'store/Delete Product.html', context)


def Search(request):
    query = request.GET.get('query', '')
    product = Product.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'store/Search.html', {'product': product, 'query': query})

def Brand(request):
    brands = Product.objects.filter(type="all")
    context = {'brands': brands}
    return render(request, 'store/Brand.html', context)


# def Category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)

#     return render(request, 'store/Category.html', {'category': category})

def Rod(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.filter(type= "rod")
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Rod Page.html', context)

def Vendor_Rod(request):
    products = Product.objects.filter(type="rod")
    context = {'products': products}
    return render(request, 'store/Vendor Rod.html', context)

def Reel (request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.filter(type = "reel")

    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Reel Page.html', context)


def Vendor_Reel(request):
    products = Product.objects.filter(type="reel")
    context = {'products': products}
    return render(request, 'store/Vendor Reel.html', context)

def Lure (request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.filter(type="lure")
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Lure Page.html', context)


def Vendor_Lure(request):
    products = Product.objects.filter(type="lure")
    context = {'products': products}
    return render(request, 'store/Vendor Lure.html', context)

def Line (request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.filter(type="line")
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Line Page.html', context)


def Vendor_Line(request):
    products = Product.objects.filter(type="line")
    context = {'products': products}
    return render(request, 'store/Vendor Line.html', context)

def Accessories (request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
            user=user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.filter(type="accessories")
    
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/Accessories Page.html', context)


def Vendor_Accessories(request):
    products = Product.objects.filter(type="accessories")
    context = {'products': products}
    return render(request, 'store/Vendor Accessories.html', context)

def Cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/Cart.html', context)

def Checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST, request.FILES)

        if form.is_valid():
                Checkout = form.save(commit=False)
                Checkout.user = request.user
                Checkout.slug = slugify(Checkout.name)
                Checkout.save()
                messages.success(request, 'Your Payment is Successful!')
                return redirect('Rod Page')
    else:
        form = CheckoutForm()

    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'form': form}
    return render (request, 'store/Checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        user=user, complete=False)

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

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)


    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(
        user=user, complete=False)
    else:
        user, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
        order.save()

    if order.shipping == True:
        Checkout.objects.create(
        user=user,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        image=data['shipping']['image'],
		)
    
    if forms.is_valid():
        image = Form.save(commit=False)
        image.user_id = request.user.id
        image.save()

    return JsonResponse('Payment submitted..', safe=False)

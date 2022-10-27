from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Checkout
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'type', 'brand','description', 'image']

class CheckoutForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length= 100)
    phone_number=forms.IntegerField()
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    zipcode = forms.IntegerField()
    state = forms.CharField(max_length=50)

    class Meta:
        model = Checkout
        fields = ['name', 'email', 'address', 'city', 'zipcode', 'state', 'image']


class CheckoutForm (ModelForm):
    class Meta:
        model = Checkout
        fields = ['image']

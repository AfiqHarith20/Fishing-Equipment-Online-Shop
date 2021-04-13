from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.Login, name="Login"),
    path('register/', views.Register, name="Register"),

    path('', views.index, name="Main Page"),
    path('rod/', views.Rod, name="Rod Page"),
    path('reel/', views.Reel, name="Reel Page"),
    path('lure/', views.Lure, name="Lure Page"),
    path('line/', views.Line, name="Line Page"),
    path('accessories/', views.Accessories, name="Accessories Page"),
    path('cart/', views.Cart, name="Cart"),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('increase_quantity/<int:item_id>',
         views.increase_quantity_item, name="increase_quantity"),
    path('decrease_quantity/<int:item_id>',
         views.decrease_quantity_item, name="decrease_quantity"),
    ]

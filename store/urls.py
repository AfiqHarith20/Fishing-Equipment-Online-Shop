from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='store/Login.html'), name="Login"),
    path('register/', views.Register, name="Register"),
    
    path('Vendor_Login/', auth_views.LoginView.as_view(
        template_name='store/Vendor Login.html'), name="Vendor Login"),
    path('Vendor_Register/', views.Vendor_Register, name="Vendor Register"),

    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),

    path('', views.index, name="Main Page"),
    path('rod/', views.Rod, name="Rod Page"),
    path('reel/', views.Reel, name="Reel Page"),
    path('lure/', views.Lure, name="Lure Page"),
    path('line/', views.Line, name="Line Page"),
    path('accessories/', views.Accessories, name="Accessories Page"),
    path('product_detail/<int:pk>/', views.Item.as_view(), name="Product Detail"),
    path('cart/', views.Cart, name="Cart"),
    path('checkout/', views.Checkout, name="Checkout"),

    path('vendor_page/', views.Vendor_Page, name="Vendor Page"),
    path('vendor_rod/', views.Vendor_Rod, name="Vendor Rod"),
    path('vendor_reel/', views.Vendor_Reel, name="Vendor Reel"),
    path('vendor_line/', views.Vendor_Line, name="Vendor Line"),
    path('vendor_lure/', views.Vendor_Lure, name="Vendor Lure"),
    path('vendor_accessories/', views.Vendor_Accessories, name="Vendor Accessories"),
    path('add_product/', views.Add_Product, name="Add Product"),
    path('product/<int:pk>/', views.Item.as_view(), name="Product"),
    path('profile/', views.Item.as_view(), name="Profile"),
    path('profile/<int:pk>/update',
         views.UserUpdate.as_view(), name="Update Profile"),
    path('product/<int:pk>/update',
         views.ItemUpdate.as_view(), name="Update Product"),
    path('delete_product/<int:pk>', views.deleteProduct, name="Delete Product"),

    path('search/', views.Search, name='Search'),
    #path('<slug:category_slug>/', views.Category, name='Category'),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('increase_quantity/<int:item_id>',
         views.increase_quantity_item, name="increase_quantity"),
    path('decrease_quantity/<int:item_id>',
         views.decrease_quantity_item, name="decrease_quantity"),
     
    ]

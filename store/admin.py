from django.contrib import admin

# Register your models here.
from.models import *
from.models import Vendor

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Checkout)




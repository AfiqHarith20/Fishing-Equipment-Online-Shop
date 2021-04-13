from django.contrib import admin

# Register your models here.
from.models import *

admin.site.register(Index_Text)
admin.site.register(Index_Image)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)



from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Login(models.Model):
    user = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=60, null=True)
    confirmPassword = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name

class Vendor (models.Model):
    name = models.CharField (max_length = 255)
    email = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name= 'vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Product(models.Model):
    name = models.CharField(max_length=60, null=True)
    price = models.DecimalField(max_digits=7, decimal_places= 2)
    type = models.CharField(max_length=60, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, max_length=60, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=600, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Product', kwargs={'pk': self.pk})

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.get_total for item in orderitems)
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitems)
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'ProductAttributes'

    def __str__(self):
        return self.product. name


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class Checkout (models.Model):
    user = models.ForeignKey(
        User, related_name='checkout', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=30, null=True)
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=40, null=True)
    zipcode = models.IntegerField(default=0)
    state = models.CharField(max_length=40, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
    		return self.address


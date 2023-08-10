from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


# Product model
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    # error handling for images with no url, @property decorator allows us to call this method like an attribute e.g product.imageURL
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# An order compilation of all order_items
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.order_items.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_quantity(self):
        order_items = self.order_items.all()
        total = sum([item.quantity for item in order_items])
        return total


# Items in the order cart
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='products_ordered')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name='order_items')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


# Shipping address
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='shipping_customer')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name='shipping_order')
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

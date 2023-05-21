import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

from decimal import Decimal

from products.models import Product
from profiles.models import UserProfile

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Please enter a valid UK postcode. Numbers and letters only.')


# handles all orders across the store
class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=11)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=8, validators=[alphanumeric])
    country = CountryField(default='GB')
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=3, decimal_places=2, default=3.99)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    original_basket = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def _generate_order_number(self):
        # Generate a random, unique order number using UUID
        return uuid.uuid4().hex.upper()

    def update_total(self):
        # Update grand total each time a line item is added
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + Decimal(self.delivery_cost)
        self.save()

    def save(self, *args, **kwargs):
        # Override the original save method to set the order number, if it hasn't been set already.
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Used to iterate through individual items in basket
# and to update delivery_cost, order_total, and grand_total
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        # Override the original save method to set the lineitem total
        # and update the order total.
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

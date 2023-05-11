from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    # Allows users to build a product wishlist
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

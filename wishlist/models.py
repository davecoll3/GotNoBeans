from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    # Link wishlist product to user
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name='wishlist')

    def __str__(self):
        return self.user.username


class WishlistItem(models.Model):
    # Items in wishlist
    wishlist = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='wishlist_products')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

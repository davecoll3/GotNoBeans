from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    # Link wishlist product to user
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False, related_name='wishlist')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    # Items in wishlist
    wishlist = models.OneToOneField(Wishlist, on_delete=models.CASCADE, null=False, blank=False, related_name='my_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='wishlist_products')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

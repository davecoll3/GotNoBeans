from django.db import models
from products.models import Product
from profiles.models import UserProfile


class FavouritesList(models.Model):
    # Links one favourites list to one user profile
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s favourites"


class FavouritesListItem(models.Model):
    # Links items to user's favourites list
    favourites = models.ForeignKey(FavouritesList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import FavouritesList, FavouritesListItem
from products.models import Product
from profiles.models import UserProfile


def favourites_list(request):
    user = get_object_or_404(UserProfile, user=request.user)
    favourites_list = FavouritesList.objects.get_or_create(user=user)
    favourites_user = favourites_list[0]
    existing_favourites = FavouritesListItem.objects.filter(favourites=favourites_user).exists()
    items = []

    if not existing_favourites:
        context = {'favourites_list': False}

        return render(request, 'favourites/favourites.html', context)

    else:
        user_favourites_list = get_list_or_404(FavouritesListItem, favourites=favourites_user)
        for product_object in user_favourites_list:
            product = get_object_or_404(Product, name=product_object)
            dates = FavouritesListItem.objects.only('added_on')
            items.append(product)
        context = {
            'favourites_list': True,
            'products': items,
            'dates': dates
        }

        return render(request, 'favourites/favourites.html', context)

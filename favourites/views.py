from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import FavouritesList, FavouritesListItem
from products.models import Product
from profiles.models import UserProfile


@login_required
def favourites_list(request):
    # Favourites list view
    user = get_object_or_404(UserProfile, user=request.user)
    favourites_list = FavouritesList.objects.get_or_create(user=user)
    favourites_user = favourites_list[0]
    existing_favourites = FavouritesListItem.objects.filter(favourites=favourites_user).exists()
    items = []

    if not existing_favourites:
        # If no existing favorites, set to false
        context = {'favourites_list': False}

        return render(request, 'favourites/favourites.html', context)

    else:
        # If existing list, set to true
        user_favourites_list = get_list_or_404(FavouritesListItem, favourites=favourites_user)
        for product_object in user_favourites_list:
            product = get_object_or_404(Product, name=product_object)
            items.append(product)
        context = {
            'favourites_list': True,
            'products': items,
        }

        return render(request, 'favourites/favourites.html', context)


@login_required
def remove_favourite(request, product_id):
    # Remove from favourites
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    favourites_list = FavouritesList.objects.get_or_create(user=user)
    favourites_user = favourites_list[0]

    if request.POST:
        product = Product.objects.get(pk=product_id)
        item_exists = FavouritesListItem.objects.filter(product=product).exists()
        if not item_exists:
            messages.error(request, "Error: this item is not one of your favourites!")
            return redirect(redirect_url)
        else:
            product = FavouritesListItem.objects.get(product=product)
            product.delete()
            messages.success(request, "Product removed from wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, 'Error: could not remove item from favourites!')
        return render(request, 'products/products.html')

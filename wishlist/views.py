from django.shortcuts import render, reverse, redirect, get_list_or_404, get_object_or_404

from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist, WishlistItem


@login_required
def wishlist(request):
    # Renders the wishlist page
    items = []
    user = UserProfile.objects.get(user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]
    existing_wishlist = WishlistItem.objects.filter(wishlist=wishlist_user).exists()

    if existing_wishlist:
        user_wishlist = get_list_or_404(WishlistItem, wishlist=wishlist_user)
        for item in user_wishlist:
            product = get_object_or_404(Product, name=item)
            items.append(product)
        context = {
            'wishlist': True,
            'products': items
        }
        return render(request, 'wishlist/wishlist.html', context)

    else:
        context = {
            'wishlist': False,
        }

    return render(request, 'wishlist/wishlist.html', context)

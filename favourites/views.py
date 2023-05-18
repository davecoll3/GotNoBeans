from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Favourites


@login_required
def favourites(request):
    """
    A view to render the users wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlists/wishlist.html', context=context)

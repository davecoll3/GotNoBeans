from django.shortcuts import render, reverse, redirect, get_object_or_404

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def wishlist(request):
    # Renders the wishlist page
    return render(request, 'wishlist/wishlist.html')

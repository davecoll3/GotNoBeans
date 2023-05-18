from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Favourites


@login_required
def favourites(request):
    # Renders the user's favourites
    favourite = None
    try:
        favourite = Favourites.objects.get(user=request.user)
    except Favourites.DoesNotExist:
        pass

    context = {
        'favourite': favourite,
    }

    return render(request, 'favourites/favourites.html', context=context)


@login_required
def remove_favourite(request, product_id):
    # Find favourites and product to remove
    favourites = Favourites.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from favourites
    favourites.products.remove(product)
    messages.info(request, "This product was removed from your favourites")

    return redirect(reverse('favourites'))

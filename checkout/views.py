from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# import stripe
import json


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are no products in your basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

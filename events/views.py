from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Event


def all_events(request):
    # A view to return all events

    events = Event.objects.all().order_by('date')

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)

from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Event
from .forms import EventForm


def all_events(request):
    # A view to return all events

    events = Event.objects.all().order_by('date')

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_event(request):
    # Add an event
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'New event added!')
            return redirect(reverse('events'))
        else:
            messages.error(request, "Failed to add event. Please ensure that the form is valid and that this event hasn't previously been created.")
    else:
        form = EventForm()

    context = {
        'form': form,
    }

    return render(request, 'events/add_event.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_event(request, event_id):
    # Delete an event
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))

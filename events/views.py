from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Event
from .forms import EventForm


def all_events(request):
    # All events view
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
        # Add event if valid
        if form.is_valid():
            event = form.save()
            messages.success(request, 'New event added!')
            return redirect(reverse('events'))
        # Display error message for invalid form
        else:
            messages.error(request, 'Please ensure that the form is valid '
                                    'and this event does not already exist.')
    else:
        form = EventForm()

    context = {
        'form': form,
    }

    return render(request, 'events/add_event.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_event(request, event_id):
    # Edit an existing event
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        # Update event if valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('events'))
        # Display error message for invalid form
        else:
            messages.error(request, 'Please ensure that the form is valid '
                                    'and this event does not already exist.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.name}')

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'events/edit_event.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_event(request, event_id):
    # Delete an event
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))

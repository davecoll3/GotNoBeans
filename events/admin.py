from django.contrib import admin
from .models import Event


class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'location',
    )

    ordering = ('date',)


admin.site.register(Event, EventsAdmin)

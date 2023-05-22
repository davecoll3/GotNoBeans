from django.contrib import admin
from .models import Event


# Admin settings for Events model
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'location',
    )

    ordering = ('date',)


admin.site.register(Event, EventsAdmin)

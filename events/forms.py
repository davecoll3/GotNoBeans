from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].label = "Event Name"
        self.fields["location"].label = "Location (cafe name etc.)"
        self.fields["street_address"].label = "Address"
        self.fields["town_or_city"].label = "Town/City"


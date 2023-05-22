from django import forms
from .models import Event


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.DateInput):
    input_type = 'time'


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': DateInput(format=('%Y-%m-%d')),
            'time': TimeInput(format=('%H:%M:%S')),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].label = "Event Name"
        self.fields["location"].label = "Location (café etc.)"
        self.fields["street_address"].label = "Address"
        self.fields["town_or_city"].label = "Town/City"

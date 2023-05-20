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
            'date': DateInput(),
            'time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].label = "Event Name"
        self.fields["location"].label = "Location (cafe name etc.)"
        self.fields["street_address"].label = "Address"
        self.fields["town_or_city"].label = "Town/City"

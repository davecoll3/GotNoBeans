from django import forms
from .widgets import CustomClearableFileInput
from .models import Recipe


class RecipeForm(forms.ModelForm):
    # Associate with Recipe model and render fields
    class Meta:
        model = Recipe
        fields = '__all__'
    # Use widget for image field
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    # Render field display names
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].label = "Recipe Name"
        self.fields["coffee_qty"].label = "Ground Coffee (grams)"
        self.fields["grind_size"].label = "Grind Size"
        self.fields["water_temp"].label = "Water Temp (°C)"
        self.fields["water_volume"].label = "Water Volume (ml)"
        self.fields["brew_time"].label = "Brew Time (mins)"
        self.fields["products"].label = "Suggested Products"
        self.fields["method"].label = "Brewing Method"

from django import forms
from .widgets import CustomClearableFileInput

from .models import Recipe, Category


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

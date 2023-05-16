from django.shortcuts import render
from .models import Recipe


def all_recipes(request):
    """ A view to return all brewing recipies """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)

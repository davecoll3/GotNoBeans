from django.shortcuts import render, reverse, get_object_or_404
from .models import Recipe

from products import views


def all_recipes(request):
    # A view to return all brewing recipies

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)


def recipe_detail(request, recipe_id):
    # A view to display individual brewing recipe details

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe_detail.html', context)

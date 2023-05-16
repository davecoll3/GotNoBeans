from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Recipe
from .forms import RecipeForm


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


def add_recipe(request):
    # Add a recipe
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added recipe!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add recipe. Please ensure the form is valid.')
    else:
        form = RecipeForm()

    template = 'recipes/add_recipe.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

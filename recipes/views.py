from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import Recipe
from .forms import RecipeForm


def all_recipes(request):
    # A view to return all brewing recipes

    recipes = Recipe.objects.all().order_by('name')

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


@user_passes_test(lambda u: u.is_superuser)
def add_recipe(request):
    # Add a recipe
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, 'New recipe added!')
            return redirect(reverse('recipe_detail', args=[recipe.id]))
        else:
            messages.error(request, 'Please ensure that the form is valid.')
    else:
        form = RecipeForm()

    context = {
        'form': form,
    }

    return render(request, 'recipes/add_recipe.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_recipe(request, recipe_id):
    # Edit an existing recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated recipe!')
            return redirect(reverse('recipe_detail', args=[recipe.id]))
        else:
            messages.error(request, 'Please ensure the form is valid.')
    else:
        form = RecipeForm(instance=recipe)
        messages.info(request, f'You are editing {recipe.name}')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/edit_recipe.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_recipe(request, recipe_id):
    # Delete a recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe successfully deleted!')
    return redirect(reverse('recipes'))

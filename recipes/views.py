from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm


def all_recipes(request):
    # All brewing recipes view
    recipes = Recipe.objects.all().order_by('name')

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/recipes.html', context)


def recipe_detail(request, recipe_id):
    # Individual brewing recipe details view
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe_detail.html', context)


@login_required
def add_recipe(request):
    # Check if superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have access.')
        return redirect(reverse('home'))
    # Add a recipe
    if request.method == 'POST':
        # Add new recipe if form is valid
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, 'New recipe added!')
            return redirect(reverse('recipe_detail', args=[recipe.id]))
        # Display error message if form is not valid
        else:
            messages.error(request, 'Please ensure that the form is valid.')
    else:
        form = RecipeForm()

    context = {
        'form': form,
    }

    return render(request, 'recipes/add_recipe.html', context)


@login_required
def edit_recipe(request, recipe_id):
    # Check if superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have access.')
        return redirect(reverse('home'))
    # Edit an existing recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        # Update recipe if form is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated recipe!')
            return redirect(reverse('recipe_detail', args=[recipe.id]))
        # Display error message if form is not valid
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


@login_required
def delete_recipe(request, recipe_id):
    # Check if superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have access.')
        return redirect(reverse('home'))
    # Delete a recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe successfully deleted!')
    return redirect(reverse('recipes'))

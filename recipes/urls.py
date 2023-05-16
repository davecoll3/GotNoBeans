from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_recipes, name='recipes'),
    path('<recipe_id>', views.recipe_detail, name='recipe_detail'),
]

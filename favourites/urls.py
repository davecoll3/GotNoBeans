from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('add_favourite/<product_id>', views.add_favourite, name='add_favourite'),
    path('remove_favourite/<product_id>', views.remove_favourite, name='remove_favourite'),
]

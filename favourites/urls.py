from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('remove_favourite/<product_id>', views.remove_favourite, name='remove_favourite'),
]

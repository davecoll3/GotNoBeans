from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites_list, name='favourites_list'),
]

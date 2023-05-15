from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites_list, name='favourites_list'),
    path('add_favourite/<int:product_id>/', views.add_favourite, name="add_favourite"),
    path('remove_favourite/<int:product_id>/', views.remove_favourite, name="remove_favourite"),
]

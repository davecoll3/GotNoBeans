from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]

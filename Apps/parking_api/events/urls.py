from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('users/', views.getUsers, name='getUsers'),
    path('events/', views.getEvents, name='getEvents'),
    path('lots/', views.getLots, name='getLots'),
]

from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('users/', views.getUsers, name='getUsers'),
    path('events/', views.getEvents, name='getEvents'),
    path('newCustomer/<str:firstName>&<str:lastName>&<str:email>&<str:password>&<int:credits>/',
        views.newCustomer, name='newCustomer'),
]

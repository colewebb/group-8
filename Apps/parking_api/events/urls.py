from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('users/', views.getUsers, name='getUsers'),
    path('users/<int:id>/', views.getUserById, name='getUserById'),
    path('events/', views.getEvents, name='getEvents'),
    path('events/<int:id>/', views.getEventById, name='getEventById'),
    path('newCustomer/<str:firstName>&<str:lastName>&<str:email>&<str:password>&<int:credits>/',
        views.newCustomer, name='newCustomer'),
]

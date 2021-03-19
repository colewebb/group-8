from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    # path('users/', views.getUsers, name='getUsers'),
    # path('users/<int:id>/', views.getUserById, name='getUserById'),
    # path('events/', views.getEvents, name='getEvents'),
    # path('events/<int:id>/', views.getEventById, name='getEventById'),
    # path('newCustomer/', views.newCustomer, name='newCustomer'),
    # path('lots/', views.getLots, name='getLots'),
    # path('lots/<int:id>/', views.getLotById, name='getLotById'),
    # path('users/<int:id>/reservations/', views.getUserReservations, name='getUserReservations'),
    path('events/', views.event_list),
    path('events/<int:pk>/', views.event_detail),
]

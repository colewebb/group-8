from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
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
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('lots/', views.LotList.as_view()),
    path('lots/<int:pk>/', views.LotDetail.as_view()),
    path('spots/', views.SpotList.as_view()),
    path('spots/<int:pk>/', views.SpotDetail.as_view()),
    path('reservations/', views.ReservationList.as_view()),
    path('reservations/<int:pk>/', views.ReservationDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

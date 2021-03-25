from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'events'
urlpatterns = [
    # general views
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('lots/', views.LotList.as_view()),
    path('lots/<int:pk>/', views.LotDetail.as_view()),
    path('reservations/', views.ReservationList.as_view()),
    path('reservations/<int:pk>/', views.ReservationDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    # more specific views
    # path('users/<int:id>/reservations/', views.UserReservationList.as_view()),
    path('events/<int:pk>/lots/', views.lotsOfEventList),
    path('users/<int:pk>/reservations/', views.reservationsOfUserList),
]

urlpatterns = format_suffix_patterns(urlpatterns)

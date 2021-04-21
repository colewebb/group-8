from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('', views.index, name='index'),
    path('get/<int:reservation_id>', views.get, name="get"),
    path('confirm/<int:reservation_id>', views.confirm, name="confirm"),
    path('deny/', views.deny, name="deny"),
    path('manual/', views.manual, name="manual"),
    path('checkin/<int:reservation_id>', views.checkin, name="checkin")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirm', views.confirm, name="confirm"),
    path('deny', views.deny, name="deny"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('manual/<int:lot_id>', views.manual, name="manual")
]
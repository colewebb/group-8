from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/<int:reservation_id>', views.get, name="get"),
    path('confirm/<int:reservation_id>', views.confirm, name="confirm"),
    path('deny/', views.deny, name="deny"),
    path('manual/', views.manual, name="manual")
]
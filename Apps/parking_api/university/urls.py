from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lot/<int:lot_id>', views.lotDetail, name="lotDetail"),
    path('add-new', views.addNew, name="addNew"),
    path('help', views.help, name="help"),
    path('logout', views.logout, name="logout"),
    path('modify-lot/<int:lot_id>', views.modifyLot, name="modifyLot"),
    path('transfer-balance', views.transferBalance, name="transferBalance"),
    path('login', views.login, name="login"),
    path('associate/<int:lot_id>', views.associate, name="associate"),
]

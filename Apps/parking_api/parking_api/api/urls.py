#from django.conf.urls import path
from django.conf.urls import url, include

from parking_api.api.views import(
    registration_view,
    )

app_name = "account"

urlpatterns = [
    #path('register', registration_view, name="register"),
    url(r'register', include('parking_api.api.urls', 'registration_view'))

]

from django import forms

class Login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ManualInput(forms.Form):
    reservationID = forms.IntegerField(label="Reservation ID")
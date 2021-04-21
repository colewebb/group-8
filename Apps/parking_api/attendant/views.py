from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import Lot, Reservation
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import *

def allowed(user):
    if user.is_staff:
        print("Staff")
        return True
    if user.groups.filter(name="Owners"):
        print("Owner")
        return True
    if user.groups.filter(name="Attendants"):
        print("Attendant")
        return True
    return False

def index(request):
    return redirect("./manual")

def confirm(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    return render(request, "attendant/confirm.html", {'reservation': reservation})

def deny(request):
    return render(request, "attendant/deny.html")

def manual(request):
    if request.method == "GET":
        form = ManualInput()
        return render(request, 'attendant/manual.html', {'form': form})
    else:
        try:
            reservation = Reservation.objects.get(pk=request.POST['reservationID'])
            return redirect("../confirm/" + str(reservation.id))
        except Reservation.DoesNotExist:
            return redirect("../deny/")

def get(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
        return redirect("../confirm/" + str(reservation.id))
    except Reservation.DoesNotExist:
        return redirect("../deny/")

def login(request):
    if request.user.is_authenticated:
        return redirect('./')
    if request.method == "GET":
        form = Login()
        return render(request, 'attendant/login.html', {'form': form})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if allowed(user):
            auth_login(request, user)
            return redirect('./')
        else:
            return render(request, "attendant/403.html")


def logout(request):
    auth_logout(request)
    return render(request, 'attendant/logout.html')

def checkin(request, reservation_id):
    return HttpResponse("Check in #" + str(reservation_id))
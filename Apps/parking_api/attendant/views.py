from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import Lot, Reservation
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .forms import *

def allowed(user):
    if user.is_staff:
        return True
    if user.groups.filter(name="Owners"):
        return True
    if user.groups.filter(name="Attendants"):
        return True
    return False

def index(request):
    if allowed(request.user):
        return redirect("./manual")
    else:
        return render(request, "attendant/403.html")

def confirm(request, reservation_id):
    if allowed(request.user):
        reservation = Reservation.objects.get(pk=reservation_id)
        return render(request, "attendant/confirm.html", {'reservation': reservation, 'user': request.user})
    else:
        return render(request, "attendant/403.html")

def deny(request):
    if allowed(request.user):
        return render(request, "attendant/deny.html", {'user': request.user})
    else:
        return render(request, "attendant/403.html")

def manual(request):
    if allowed(request.user):
        if request.method == "GET":
            form = ManualInput()
            return render(request, 'attendant/manual.html', {'form': form, 'user': request.user})
        else:
            try:
                reservation = Reservation.objects.get(pk=request.POST['reservationID'])
                if reservation.consumed:
                    return redirect("../deny/")
                return redirect("../confirm/" + str(reservation.id))
            except Reservation.DoesNotExist:
                return redirect("../deny/")
    else:
        return render(request, "attendant/403.html")

def get(request, reservation_id):
    if allowed(request.user):
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
            if reservation.consumed:
                    return redirect("../deny/")
            return redirect("../confirm/" + str(reservation.id))
        except Reservation.DoesNotExist:
            return redirect("../deny/")
    else:
        return render(request, "attendant/403.html")

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
    if allowed(request.user):
        reservation = Reservation.objects.get(pk=reservation_id)
        reservation.consumed = True
        reservation.save()
        return render(request, "attendant/checkin.html", {'user': request.user})
    else:
        return render(request, "attendant/403.html")
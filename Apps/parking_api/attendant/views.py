from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import Lot, Reservation
from .forms import *

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
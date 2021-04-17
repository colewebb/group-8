from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from api.models import Lot
from .forms import *

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("./login")
    lots = Lot.objects.filter(owner=request.user)
    return render(request, "attendant/index.html", {'lots': lots, 'user': request.user})

def attend(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./')
    return render(request, "attendant/attend.html", {'user': request.user})

def confirm(request):
    if not request.user.is_authenticated:
        return redirect('./')
    return render(request, "attendant/confirm.html", {'user': request.user})

def deny(request):
    if not request.user.is_authenticated:
        return redirect('./')
    return render(request, "attendant/deny.html", {'user': request.user})

def login(request):
    if request.user.is_authenticated:
        return redirect('./')
    if request.method == "GET":
        form = Login()
        return render(request, 'attendant/login.html', {'form': form})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('./')
        else:
            return render(request, 'attendant/logout.html')

def logout(request):
    auth_logout(request)
    return render(request, 'attendant/logout.html')

def manual(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./')
    return render(request, 'attendant/manual.html', {'user': request.user})
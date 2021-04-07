from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from api.models import Lot, ParentLot
from .forms import *

def urlEncodeAddress(path):
    path = path.split(" ")
    toReturn = ""
    for bit in path:
        toReturn = toReturn + bit + "+"
    return toReturn[:-1]

def index(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    lots = ParentLot.objects.order_by('id')
    context = {'lots': lots, 'user': request.user}
    return render(request, 'lotOwners/index.html', context)


def lotDetail(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./login')
    lot = ParentLot.objects.get(pk=lot_id)
    context = {'lot': lot, 'user': request.user, 'safeAddress': urlEncodeAddress(lot.address)}
    return render(request, 'lotOwners/lot.html', context)


def addNew(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    form = NewLotForm()
    return render(request, "lotOwners/add-new.html", {'form': form, 'user': request.user})


def help(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    return render(request, 'lotOwners/help.html', {'user': request.user})


def logout(request):
    auth_logout(request)
    return render(request, 'lotOwners/logout.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('./')
    if request.method == "GET":
        form = Login()
        return render(request, 'lotOwners/login.html', {'form': form})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('./')
        else:
            return render(request, 'lotOwners/logout.html')


def modifyLot(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./login')
    lot = ParentLot.objects.get(pk=lot_id)
    form = ModifyLotForm(initial={
        'lotName': lot.name,
        'lotAddress': lot.address
    })
    context = {
        'lot': lot,
        'form': form,
        'user': request.user
    }
    return render(request, 'lotOwners/modify.html', context)


def transferBalance(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    form = TransferBalance()
    return render(request, 'lotOwners/transfer-balance.html', {'form': form, 'user': request.user})

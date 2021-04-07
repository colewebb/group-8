from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from api.models import Lot, ParentLot
from .forms import *

def urlEncodeAddress(path):
    path = path.split(" ")
    toReturn = ""
    for bit in path:
        toReturn = toReturn + bit + "+"
    return toReturn[:-1]

def index(request):
    lots = ParentLot.objects.order_by('id')
    context = {'lots': lots}
    return render(request, 'lotOwners/index.html', context)


def lotDetail(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    context = {'lot': lot, 'safeAddress': urlEncodeAddress(lot.address)}
    return render(request, 'lotOwners/lot.html', context)


def addNew(request):
    form = NewLotForm()
    return render(request, "lotOwners/add-new.html", {'form': form})


def help(request):
    return render(request, 'lotOwners/help.html')


def logout(request):
    # logout token bullcrap will need to go here
    return render(request, 'lotOwners/logout.html')


def login(request):
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
    lot = ParentLot.objects.get(pk=lot_id)
    form = ModifyLotForm(initial={
        'lotName': lot.name,
        'lotAddress': lot.address
    })
    context = {
        'lot': lot,
        'form': form
    }
    return render(request, 'lotOwners/modify.html', context)


def transferBalance(request):
    form = TransferBalance()
    return render(request, 'lotOwners/transfer-balance.html', {'form': form})

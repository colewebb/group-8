from django.shortcuts import render
from django.http import HttpResponse
from api.models import Lot
from .forms import *

def urlEncodeAddress(path):
    path = path.split(" ")
    toReturn = ""
    for bit in path:
        toReturn = toReturn + bit + "+"
    return toReturn[:-1]

def index(request):
    lots = Lot.objects.order_by('id')
    context = {'lots': lots}
    return render(request, 'lotOwners/index.html', context)


def lotDetail(request, lot_id):
    lot = Lot.objects.get(pk=lot_id)
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
    form = Login()
    return render(request, 'lotOwners/login.html', {'form': form})


def modifyLot(request, lot_id):
    lot = Lot.objects.get(pk=lot_id)
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

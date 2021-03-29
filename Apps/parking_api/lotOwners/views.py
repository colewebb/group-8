from django.shortcuts import render
from django.http import HttpResponse
from api.models import Lot

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
    return render(request, "lotOwners/add-new.html")


def help(request):
    return render(request, 'lotOwners/help.html')


def logout(request):
    # logout token bullcrap will need to go here
    return render(request, 'lotOwners/logout.html')


def modifyLot(request, lot_id):
    lot = Lot.objects.get(pk=lot_id)
    context = {'lot': lot}
    return render(request, 'lotOwners/modify.html', context)


def transferBalance(request):
    return render(request, 'lotOwners/transfer-balance.html')

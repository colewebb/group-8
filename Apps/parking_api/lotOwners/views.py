from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from api.models import Lot, ParentLot, Event
from datetime import datetime
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
    lots = ParentLot.objects.filter(owner=request.user)
    events = Lot.objects.filter(owner=request.user)
    context = {'lots': lots, 'user': request.user, 'events': events}
    return render(request, 'lotOwners/index.html', context)


def lotDetail(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    context = {'lot': lot, 'safeAddress': urlEncodeAddress(lot.address), 'user': request.user}
    return render(request, 'lotOwners/lot.html', context)


def addNew(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('./login')
        form = NewLotForm()
        return render(request, "lotOwners/add-new.html", {'form': form, 'user': request.user})
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('../login')
        newLot = ParentLot(
            name=request.POST['lotName'],
            created=datetime.now(),
            address=request.POST['lotAddress'],
            owner=request.user,
            capSmallMax=request.POST['smallSpotCount'],
            capMediumMax=request.POST['mediumSpotCount'],
            capLargeMax=request.POST['oversizeSpotCount']
        )
        newLot.save()
        return redirect("./lot/" + str(newLot.id))


def help(request):
    return render(request, 'lotOwners/help.html', {'user': request.user})


def logout(request):
    logout(request)
    return render(request, 'lotOwners/logout.html')


def login(request):
    form = Login()
    return render(request, 'lotOwners/login.html', {'form': form})


def modifyLot(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('../login')
        if lot.owner != request.user:
            return redirect('../login')
        form = ModifyLotForm(initial={
            'lotName': lot.name,
            'lotAddress': lot.address,
            'smallSpotCount': lot.capSmallMax,
            'mediumSpotCount': lot.capMediumMax,
            'oversizeSpotCount': lot.capLargeMax
        })
        context = {
            'lot': lot,
            'form': form,
            'user': request.user
        }
        return render(request, 'lotOwners/modify.html', context)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('../login')
        if lot.owner != request.user:
            return redirect('../login')
        lot.name = request.POST['lotName']
        lot.address = request.POST['lotAddress']
        lot.capSmallMax = request.POST['smallSpotCount']
        lot.capMediumMax = request.POST['mediumSpotCount']
        lot.capLargeMax = request.POST['oversizeSpotCount']
        lot.save()
        return redirect("../lot/" + str(lot_id))


def associate(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    events = Event.objects.all()
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('../login')
        if lot.owner != request.user:
            return redirect('../login')
        form = AssociateWithEvent(initial={
            'capSmallActual': lot.capSmallMax,
            'capMediumActual': lot.capMediumMax,
            'capLargeActual': lot.capLargeMax
        })
        return render(request, 'lotOwners/associate.html', {'user': request.user, 'lot': lot, 'events': events, 'form': form})
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('../login')
        if lot.owner != request.user:
            return redirect('../login')
        a = Lot(
            created=datetime.now(),
            owner=request.user,
            capSmallMax=lot.capSmallMax,
            capMediumMax=lot.capMediumMax,
            capLargeMax=lot.capLargeMax,
            openTime=request.POST['openTime'],
            closeTime=request.POST['closeTime'],
            costSmall=request.POST['costSmall'],
            capSmallActual=request.POST['capSmallActual'],
            costMedium=request.POST['costMedium'],
            capMediumActual=request.POST['capMediumActual'],
            costLarge=request.POST['costLarge'],
            capLargeActual=request.POST['capLargeActual'],
            event=Event.objects.get(pk=request.POST['event']),
            parentLot=lot
        )
        a.save()
        return redirect("../")


def transferBalance(request):
    form = TransferBalance()
    return render(request, 'lotOwners/transfer-balance.html', {'form': form, 'user': request.user})

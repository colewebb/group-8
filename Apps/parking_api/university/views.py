from django.shortcuts import render, redirect
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
    lots = ParentLot.objects.all()
    events = Lot.objects.all()
    context = {'lots': lots, 'user': request.user, 'events': events}
    return render(request, 'university/index.html', context)


def lotDetail(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./login')
    lot = ParentLot.objects.get(pk=lot_id)
    context = {'lot': lot, 'user': request.user, 'safeAddress': urlEncodeAddress(lot.address)}
    return render(request, 'university/lot.html', context)


def addNew(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('./login')
        form = NewLotForm()
        return render(request, "university/add-new.html", {'form': form, 'user': request.user})
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
    if not request.user.is_authenticated:
        return redirect('./login')
    return render(request, 'university/help.html', {'user': request.user})


def logout(request):
    auth_logout(request)
    return render(request, 'university/logout.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('./')
    if request.method == "GET":
        form = Login()
        return render(request, 'university/login.html', {'form': form})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('./')
        else:
            return render(request, 'university/logout.html')


def modifyLot(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    if request.method == "GET":
        if not request.user.is_authenticated:
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
        return render(request, 'university/modify.html', context)
    if request.method == "POST":
        if not request.user.is_authenticated:
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
        form = AssociateWithEvent(initial={
            'capSmallActual': lot.capSmallMax,
            'capMediumActual': lot.capMediumMax,
            'capLargeActual': lot.capLargeMax
        })
        return render(request, 'university/associate.html', {'user': request.user, 'lot': lot, 'events': events, 'form': form})
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
    if not request.user.is_authenticated:
        return redirect('./login')
    form = TransferBalance()
    return render(request, 'university/transfer-balance.html', {'form': form, 'user': request.user})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from api.models import Lot, ParentLot, Event, Balance
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
    if request.user.groups.filter(name="Owners"):
        lots = ParentLot.objects.filter(owner=request.user)
        events = Lot.objects.filter(owner=request.user)
        balance = Balance.objects.get(owner=request.user)
        context = {'lots': lots, 'user': request.user, 'events': events, 'balance': balance}
        return render(request, 'lotOwners/index.html', context)
    else:
        return render(request, "lotOwners/403.html")

def lotDetail(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./login')
    if request.user.groups.filter(name="Owners"):
        lot = ParentLot.objects.get(pk=lot_id)
        context = {'lot': lot, 'user': request.user, 'safeAddress': urlEncodeAddress(lot.address)}
        return render(request, 'lotOwners/lot.html', context)
    else:
        return render(request, "lotOwners/403.html")


def addNew(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('./login')
        if request.user.groups.filter(name="Owners"):
            form = NewLotForm()
            return render(request, "lotOwners/add-new.html", {'form': form, 'user': request.user})
        else:
            return render(request, "lotOwners/403.html")
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('../login')
        if request.user.groups.filter(name="Owners"):
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
        else:
            return render(request, "lotOwners/403.html")


def help(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    if request.user.groups.filter(name="Owners"):
        return render(request, 'lotOwners/help.html', {'user': request.user})
    else:
        return render(request, "lotOwners/403.html")


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
        if user is not None and user.groups.filter(name="Owners").exists:
            auth_login(request, user)
            return redirect('./')
        else:
            return render(request, 'lotOwners/logout.html')


def modifyLot(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('../login')
        if request.user.groups.filter(name="Owners"):
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
        else:
            return render(request, "lotOwners/403.html")
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('../login')
        if request.user.groups.filter(name="Owners"):
            lot.name = request.POST['lotName']
            lot.address = request.POST['lotAddress']
            lot.capSmallMax = request.POST['smallSpotCount']
            lot.capMediumMax = request.POST['mediumSpotCount']
            lot.capLargeMax = request.POST['oversizeSpotCount']
            lot.save()
            return redirect("../lot/" + str(lot_id))
        else:
            return render(request, "lotOwners/403.html")


def associate(request, lot_id):
    lot = ParentLot.objects.get(pk=lot_id)
    events = Event.objects.all()
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('../login')
        if request.user.groups.filter(name="Owners"):
            form = AssociateWithEvent(initial={
                'capSmallActual': lot.capSmallMax,
                'capMediumActual': lot.capMediumMax,
                'capLargeActual': lot.capLargeMax
            })
            return render(request, 'lotOwners/associate.html', {'user': request.user, 'lot': lot, 'events': events, 'form': form})
        else:
            return render(request, "lotOwners/403.html")
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('../login')
        if lot.owner != request.user:
            return redirect('../login')
        if request.user.groups.filter(name="Owners"):
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
        else:
            return render(request, "lotOwners/403.html")


def transferBalance(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    if request.method == "GET":
        if request.user.groups.filter(name="Owners"):
            form = TransferBalance()
            return render(request, 'lotOwners/transfer-balance.html', {'form': form, 'user': request.user})
        else:
            return render(request, "lotOwners/403.html")
    elif request.method == "POST":
        if request.user.groups.filter(name="Owners"):
            balance = Balance.objects.get(owner=request.user)
            transferAmount = request.POST['transferAmount']
            if float(transferAmount) > float(balance.value):
                return HttpResponse("You do not have that much money in your account. Please try again.")
            else:
                balance.value = float(balance.value) - float(transferAmount)
                balance.save()
                return redirect('./')
        else:
            return render(request, "lotOwners/403.html")

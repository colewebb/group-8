from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from api.models import Lot, ParentLot
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
    context = {'lots': lots, 'user': request.user}
    return render(request, 'lotOwners/index.html', context)


def lotDetail(request, lot_id):
    if not request.user.is_authenticated:
        return redirect('./login')
    lot = ParentLot.objects.get(pk=lot_id)
    if lot.owner != request.user:
        return redirect('../login')
    context = {'lot': lot, 'user': request.user, 'safeAddress': urlEncodeAddress(lot.address)}
    return render(request, 'lotOwners/lot.html', context)


def addNew(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('./login')
        form = NewLotForm()
        return render(request, "lotOwners/add-new.html", {'form': form, 'user': request.user})
    if request.method == "POST":
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
        return redirect("../lot/" + str(newLot.id))


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
    lot = ParentLot.objects.get(pk=lot_id)
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('./login')
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
        if request.POST['delete'] == True:
            lot.delete()
        lot.name = request.POST['lotName']
        lot.address = request.POST['lotAddress']
        lot.capSmallMax = request.POST['smallSpotCount']
        lot.capMediumMax = request.POST['mediumSpotCount']
        lot.capLargeMax = request.POST['oversizeSpotCount']
        lot.save()
        return redirect("../lot/" + str(lot_id))




def transferBalance(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    form = TransferBalance()
    return render(request, 'lotOwners/transfer-balance.html', {'form': form, 'user': request.user})

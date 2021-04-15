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
        return redirect("./lot/" + str(newLot.id))


def help(request):
    return render(request, 'lotOwners/help.html')


def logout(request):
    # logout token bullcrap will need to go here
    return render(request, 'lotOwners/logout.html')


def login(request):
    form = Login()
    return render(request, 'lotOwners/login.html', {'form': form})


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
        lot.name = request.POST['lotName']
        lot.address = request.POST['lotAddress']
        lot.capSmallMax = request.POST['smallSpotCount']
        lot.capMediumMax = request.POST['mediumSpotCount']
        lot.capLargeMax = request.POST['oversizeSpotCount']
        lot.save()
        return redirect("../lot/" + str(lot_id))




def transferBalance(request):
    form = TransferBalance()
    return render(request, 'lotOwners/transfer-balance.html', {'form': form})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Event, Lot, Spot

import json

# Create your views here.

def getUsers(request):

    response_dictionary = []
    for user in User.objects.all():
        reservation_list = []
        for reservation in user.reservation_set.all():
            res_dict = {
                # 'spotType': reservation.spotType,
                'date': str(reservation.date),
                # 'address': reservation.address,
                # 'price': reservation.price,
                'id': reservation.id,
            }
            reservation_list.append(res_dict)

        user_dict = {
            'username': user.username,
            'email': user.email,
            'reservations': reservation_list,
        }
        response_dictionary.append(user_dict)

    return JsonResponse(response_dictionary, safe=False)

def getUserById(request, id):
    try:
        user = User.objects.get(pk=id)

        reservation_list = []
        for reservation in user.reservation_set.all():
            res_dict = {
                'date': str(reservation.date),
                'id': reservation.id,
            }
            reservation_list.append(res_dict)

        user_dictionary = {
            'username': user.username,
            'email': user.email,
            'reservations': reservation_list,
        }

        return JsonResponse(user_dictionary, safe=False)
    except (User.DoesNotExist):
        error = {
            'error': f"Could not find the user corresponding with the given id '{id}'"
        }

        return JsonResponse(error, safe=False)


def newCustomer(request):
    # customer = Customer(firstName=firstName, lastName=lastName,
    #                     email=email, password=password, credits=credits)
    # customer.save()
    #
    # # eventually, return something else
    # return getUsers(request)
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    role = request.POST['role']
    credits = 500

    if username == "" or email == "" or password = "":


    new_customer = User(username=username,
                            email=email,
                            password=password,
                            role=role,
                            credits=credits
                            )
    new_customer.save()

def getEvents(request):
    response = {}

    events = []
    for event in Event.objects.all():
        dict = {
            'title': event.name,
            'address': event.address,
            'startTime': str(event.startTime),
            'endTime': str(event.endTime),
            'id': event.id,
        }
        events.append(dict)

    response['events'] = events

    return JsonResponse(response, safe=False)

def getEventById(request, id):
    try:
        event = Event.objects.get(pk=id)

        dict = {
            'title': event.name,
            'address': event.address,
            'startTime': str(event.startTime),
            'endTime': str(event.endTime),
            'id': event.id,
        }

        return JsonResponse(dict, safe=False)
    except (Event.DoesNotExist):
        dict = {
            'error': f"Could not find the event corresponding with the given id '{id}'"
        }

        return JsonResponse(dict, safe=False)

# def newEvent(request, name, startTime, endTime, address)
def getLots(request):
    response = {}

    lots = []
    for lot in Lot.objects.all():
        spot_list = []
        for spot in lot.spot_set.all():
            spot_dict = {
                'size': spot.size,
                'cost': spot.cost,
                'reserved': spot.reserved,
            }
            spot_list.append(spot_dict)

        dict = {
            'name': lot.name,
            'address': lot.address,
            'spots': spot_list,
            'openTime': lot.openTime,
            'closeTime': lot.closeTime,
            'capacityActual': lot.capacityActual,
            'capacityMax': lot.capacityMax,
        }
        lots.append(dict)

    response['lots'] = lots

    return JsonResponse(response, safe=False)

def getLotById(request, id):
    try:
        lot = Lot.objects.get(pk=id)

        spot_list = []
        for spot in lot.spot_set.all():
            spot_dict = {
                'size': spot.size,
                'cost': spot.cost,
                'reserved': spot.reserved,
            }
            spot_list.append(spot_dict)

        dict = {
            'name': lot.name,
            'address': lot.address,
            'spots': spot_list,
            'openTime': lot.openTime,
            'closeTime': lot.closeTime,
            'capacityActual': lot.capacityActual,
            'capacityMax': lot.capacityMax,
        }

        return JsonResponse(dict, safe=False)
    except (Lot.DoesNotExist):
        dict = {
            'error': f"Could not find the lot corresponding with the given id '{id}'"
        }

        return JsonResponse(dict, safe=False)

def getUserReservations(request, id):
    try:
        customer = Customer.objects.get(pk=id)

        res_list = []
        for reservation in customer.reservation_set.all():
            spot = reservation.spot
            lot = spot.lot
            event = reservation.event
            res_dict = {
                'spot': {
                    'size': spot.size,
                    'cost': spot.cost,
                },
                'lot': {
                    'name': lot.name,
                    'address': lot.address,
                    'openTime': lot.openTime,
                    'closeTime': lot.closeTime,
                    'capacityActual': lot.capacityActual,
                    'capacityMax': lot.capacityMax,
                },
                'event': {
                    'title': event.name,
                    'address': event.address,
                    'startTime': str(event.startTime),
                    'endTime': str(event.endTime),
                    'id': event.id,
                },
            }

            res_list.append(res_dict)

        response = {'reservations': res_list}

        return JsonResponse(response, safe=False)


    except (Customer.DoesNotExist):
        dict = {
            'error': f"Could not find the user corresponding with the given id '{user_id}'"
        }

        return JsonResponse(dict, safe=False)

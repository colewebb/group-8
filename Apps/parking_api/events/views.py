from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Event, Lot, Spot

import json

# Create your views here.

def getUsers(request):

    response_dictionary = []
    for customer in Customer.objects.all():
        reservation_list = []
        for reservation in customer.reservation_set.all():
            res_dict = {
                'spotType': reservation.spotType,
                'date': str(reservation.date),
                'address': reservation.address,
                'price': reservation.price,
                'id': reservation.id,
            }
            reservation_list.append(res_dict)

        customer_dictionary = {
            'firstName': customer.firstName,
            'lastName': customer.lastName,
            'email': customer.email,
            'reservations': reservation_list,
        }
        response_dictionary.append(customer_dictionary)

    return JsonResponse(response_dictionary, safe=False)

def getUserById(request, id):
    try:
        user = Customer.objects.get(pk=id)

        reservation_list = []
        for reservation in user.reservation_set.all():
            res_dict = {
                'spotType': reservation.spotType,
                'date': str(reservation.date),
                'address': reservation.address,
                'price': reservation.price,
                'id': reservation.id,
            }
            reservation_list.append(res_dict)

        user_dictionary = {
            'firstName': user.firstName,
            'lastName': user.lastName,
            'email': user.email,
            'reservations': reservation_list,
        }

        return JsonResponse(user_dictionary, safe=False)
    except (Customer.DoesNotExist):
        error = {
            'error': f"Could not find the user corresponding with the given id '{id}'"
        }

        return JsonResponse(error, safe=False)


def newCustomer(request, firstName, lastName, email, password, credits):
    customer = Customer(firstName=firstName, lastName=lastName,
                        email=email, password=password, credits=credits)
    customer.save()

    # eventually, return something else
    return getUsers(request)

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
        #spot_list = lot.spot_set()
        dict = {
            'name': lot.name,
            'address': lot.address,
        #    'spots': spot_list,
            'openTime': lot.openTime,
            'closeTime': lot.closeTime,
            'capacityActual': lot.capacityActual,
            'capacityMax': lot.capacityMax,
        }
        lots.append(dict)

    response['lots'] = lots

    return JsonResponse(response, safe=False)

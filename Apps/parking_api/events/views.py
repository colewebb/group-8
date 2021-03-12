from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Event, Lot, Spot

import json

# Create your views here.

def getUsers(request):

    response_dictionary = []
    for customer in Customer.objects.all():
        customer_dictionary = {
            'firstName': customer.firstName,
            'lastName': customer.lastName,
            'email': customer.email,
        }
        response_dictionary.append(customer_dictionary)

    return JsonResponse(response_dictionary, safe=False)

def getEvents(request):
    response = {}

    events = []
    for event in Event.objects.all():
        dict = {
            'title': event.name,
            'address': event.address,
            'startTime': str(event.startTime),
            'endTime': str(event.endTime),
        }
        events.append(dict)

    response['events'] = events

    return JsonResponse(response, safe=False)

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

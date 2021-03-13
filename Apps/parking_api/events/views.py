from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Event

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
        }
        events.append(dict)

    response['events'] = events

    return JsonResponse(response, safe=False)

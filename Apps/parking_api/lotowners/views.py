from django.shortcuts import render
from api.models import *


def index(request):
    return render(request, 'lotowners/index.html', {})

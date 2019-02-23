from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from api.script import *

def index(request):
    return render(request, 'index.html', context={'id': 1})

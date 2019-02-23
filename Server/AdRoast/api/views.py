from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from api.script import *

# Create your views here.
@csrf_exempt
def analysisGET(request):
    print('GET Request Recieved :' + request.method + str(request))
    if request.method == 'GET':
        data = {
            'id': '1',
            'param1': testscript(),
            'param2': 'Your ad sucks',
            'param3': 'Try again.'
        }
        return JsonResponse(data)
    else:
        return HttpResponseBadRequest(str(request));

@csrf_exempt
def analysisPOST(request):
    print('POST Request Recieved :' + request.method + request.body + request.POST)
    if request.method == 'POST':
        data = {
            'response': 'It was a POST Request'
        }
        return JsonResponse(data)
    else:
        data = {
            'response': '8===D'
        }
        return JsonResponse(data)

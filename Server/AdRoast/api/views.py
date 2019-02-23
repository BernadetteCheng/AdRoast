from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from api.script import *

# Create your views here.
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

def analysisPOST(request):
    print('POST Request Recieved :' + request.method + str(request))
    if request.method == 'POST':
        return HttpResponseBadRequest(str(request));
    else:
        return HttpResponseBadRequest(str(request));

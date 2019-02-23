from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from testscript import *

# Create your views here.
def analysisGET(request):
    print('GET Request Recieved :' + request.method)
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

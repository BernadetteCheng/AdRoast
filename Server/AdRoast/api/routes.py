from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from api.FeatureServerExtraction import *

@csrf_exempt
def analysisPOST(request):
    print('POST Request Recieved :' + request.method)
    if request.method == 'POST':
        with open("parsedImage.jpg", "wb") as fh:
            fh.write(base64.decodebytes(request.body))
        result = extract_feature("P1.jpg")
        data = {
            'grade': str(result[0]),
            'improvements': result[1],
            'reg': result[2]
        }
        return JsonResponse(data)
        """
        print('P1')
        print('1:' + result[0])
        print('2:' + str(result[1]))
        print('3:' + str(result[2]))
        result = extract_feature("P2.jpg")
        data = {
            'grade': result[0],
            'improvements': result[1],
            'score': result[2]
        }

        print('P2')
        print('1:' + result[0])
        print('2:' + str(result[1]))
        print('3:' + str(result[2]))

        result = extract_feature("P3.jpg")
        data = {
            'grade': result[0],
            'improvements': result[1],
            'score': result[2]
        }
        print('P3')
        print('1:' + result[0])
        print('2:' + str(result[1]))
        print('3:' + str(result[2]))

        result = extract_feature("P4.jpg")
        data = {
            'grade': result[0],
            'improvements': result[1],
            'score': result[2]
        }
        print('P4')
        print('1:' + result[0])
        print('2:' + str(result[1]))
        print('3:' + str(result[2]))

        result = extract_feature("P5.jpg")
        data = {
            'grade': result[0],
            'improvements': result[1],
            'score': result[2]
        }
        print('P5')
        print('1:' + result[0])
        print('2:' + str(result[1]))
        print('3:' + str(result[2]))
        """
    else:
        data = {
            'response': 'Not a POST request'
        }
        return JsonResponse(data)

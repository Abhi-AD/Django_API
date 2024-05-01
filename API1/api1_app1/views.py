import json
from django.shortcuts import render

from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from api1_app2.models import Product
from api1_app2.serializers import ProductSerializers



def api_home(request, *args, **kwargs):
     print(request.GET)
     print(request.POST)
     body = request.body  # JSON DATA
     data = {}
     try:
          data = json.loads(body)  # byte string of JSON data -> python dict
     except:
        pass
     print(data)
     
     data['params'] = dict(request.GET)
     data["headers"] = dict(request.headers)  # requests.META
     data["content_type"] = request.content_type

     return JsonResponse(data)



@api_view(["POST"])
def api2_home(request, *args, **kwargs):
     """
     DRF API VIEW
     """
     serializer = ProductSerializers(data=request.data)
     if serializer.is_valid(raise_exception=True):
          print(serializer.data)
          return Response(serializer.data)
     return Response({"invalid":"Not a Good Data Insert"}, status=400)


import json
from django.shortcuts import render
from django.http import JsonResponse


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

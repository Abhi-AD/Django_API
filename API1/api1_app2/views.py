import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from api1_app2.models import Product

# def api2_home(request, *args, **kwargs):
#      Model_data = Product.objects.all().order_by("?").first()
#      data = {}
#      if Model_data:
#           data['id'] = Model_data.id
#           data['title'] = Model_data.title
#           data['content'] = Model_data.content
#           data['price'] = Model_data.price
#      return JsonResponse(data)

def api2_home(request, *args, **kwargs):
     Model_data = Product.objects.all().order_by("?").first()
     data = {}
     if Model_data:
          data = model_to_dict(Model_data, fields=['id','title','content','price'])
     return JsonResponse(data)
          # json_data = json.dumps(data)
     # return HttpResponse(json_data, headers={"content-type":"application/json"})

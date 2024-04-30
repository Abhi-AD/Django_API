import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api1_app2.models import Product
from api1_app2.serializers import ProductSerializers

# def api2_home(request, *args, **kwargs):
#      Model_data = Product.objects.all().order_by("?").first()
#      data = {}
#      if Model_data:
#           data['id'] = Model_data.id
#           data['title'] = Model_data.title
#           data['content'] = Model_data.content
#           data['price'] = Model_data.price
#      return JsonResponse(data)




@api_view(["GET"])
def api2_home(request, *args, **kwargs):
     """
     DRF API VIEW
     """
     instance = Product.objects.all().order_by("?").first()
     data = {}
     if instance:
          # data = model_to_dict(instance, fields=['id','title','content','price','sale_price'])
          data=ProductSerializers(instance).data
     return Response(data)
          # json_data = json.dumps(data)
     # return HttpResponse(json_data, headers={"content-type":"application/json"})

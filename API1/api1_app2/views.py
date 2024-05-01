import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from api1_app2.models import Product
from api1_app2.serializers import ProductSerializers


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get(
            "content", None
        )  

        if content is None:
            content = title 
        serializer.save(content=content)
        # send a signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

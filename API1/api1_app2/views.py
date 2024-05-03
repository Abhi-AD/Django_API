from django.shortcuts import get_object_or_404

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
        content = serializer.validated_data.get("content", None)

        if content is None:
            content = title
        serializer.save(content=content)
        # send a signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
   

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    def perform_destory(self,instance):
        super().perform_destory(instance)
            


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializers(obj,many=False).data
            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerializers(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content", None)
            
            if content is None:
                content = title
                
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Not a Good Data Insert"}, status=400)

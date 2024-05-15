from rest_framework import viewsets, mixins
from api1_app2.models import Product
from api1_app2.serializers import ProductSerializers


class ProductsViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> products instance detail view
    post -> create -> new instance
    put -> update
    patch -> partial update
    delete -> destory
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"  # default id


class ProductsGenericViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    get -> list -> queryset
    get -> retrieve -> products instance detail view
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"  # default id

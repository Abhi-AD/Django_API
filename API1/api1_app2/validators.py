from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api1_app2.models import Product

# def validate_title(value):
#     data = Product.objects.filter(title__iexact=value)
#     if data.exists():
#         raise serializers.ValidationError(f"{value} is already a product name...!")
#     return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is already a product name...!")
    return value
unique_product_title =UniqueValidator(queryset=Product.objects.all())
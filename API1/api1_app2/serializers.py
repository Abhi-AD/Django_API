from rest_framework import serializers
from rest_framework.reverse import reverse
from api1_app2.models import Product
from api1_app2.validators import validate_title_no_hello, unique_product_title
from api1_app2 import validators


class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title]
    )
    name = serializers.CharField(source = "title", read_only=True)

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "pk",
            "name",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    # def validate_title(self,value):
    #     request = self.context.get('request')
    #     user = request.user()
    #     data = Product.objects.filter(user=user,title__iexact=value)
    #     if data.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name...!")
    #     return value

    # def create(self, validated_data):
    #     obj =  super().create(validated_data)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

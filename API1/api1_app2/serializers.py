from rest_framework import serializers
from rest_framework.reverse import reverse
from api1_app2.models import Product


class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]
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

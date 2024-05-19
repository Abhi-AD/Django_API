from rest_framework import serializers
from rest_framework.reverse import reverse
from api1_app1.serializers import UserPublicSerializer
from api1_app2.models import Product
from api1_app2.validators import validate_title_no_hello, unique_product_title
from api1_app2 import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializers(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title]
    )
    name = serializers.CharField(source="title", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Product
        fields = [
            "owner",
            "url",
            "edit_url",
            "pk",
            "name",
            "email",
            "title",
            "content",
            "price",
            "sale_price",
        ]

    def get_data(self, obj):
        return {"username": obj.user.username}

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

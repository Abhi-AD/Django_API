from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    this_is_not_realfield = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)


#     other = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#          model = User
#          fields = [
#               'username',
#               'this_is_not_realfield',
#               'id',
#          ]


#     def get_other(self, obj):
#         user = obj
#         product = user.product_set.all()[:5]
#         return UserProductInlineSerializer(product, many=True,context=self.context).data

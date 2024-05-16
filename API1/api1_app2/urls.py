from django.urls import path
from api1_app2 import views
from api1_app2.views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
    ProductMixinView,
)

urlpatterns = [
    path("create/", ProductListCreateAPIView.as_view(), name="product-list"),
    path("detail/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("update/<int:pk>/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("delete/<int:pk>/", ProductDestroyAPIView.as_view(), name="product-delete"),
]

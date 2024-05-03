from django.urls import path
from api1_app2 import views
from api1_app2.views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    ProductUpdateAPIView,
    ProductDestroyAPIView,
)

urlpatterns = [
    path("create/", ProductListCreateAPIView.as_view(), name="create"),
    path("detail/<int:pk>/", ProductDetailAPIView.as_view(), name="detail"),
    path("update/<int:pk>/", ProductUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", ProductDestroyAPIView.as_view(), name="delete"),
]

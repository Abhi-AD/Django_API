from django.urls import path
from api1_app2.views import ProductDetailAPIView, ProductListCreateAPIView

urlpatterns = [
    path("create/", ProductListCreateAPIView.as_view(), name="create"),
    path("detail/<int:pk>/", ProductDetailAPIView.as_view(), name="detail"),
]

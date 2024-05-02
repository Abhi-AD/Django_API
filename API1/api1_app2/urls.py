from django.urls import path
from api1_app2 import views
from api1_app2.views import ProductDetailAPIView, ProductListCreateAPIView

urlpatterns = [
    path("create/", ProductListCreateAPIView.as_view(), name="create"),
    path("detail/<int:pk>/", ProductDetailAPIView.as_view(), name="detail"),
    # path("create/", views.product_alt_view),
    # path("detail/<int:pk>/", views.product_alt_view)
]

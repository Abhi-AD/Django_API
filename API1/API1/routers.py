from rest_framework.routers import DefaultRouter
from api1_app2.viewset import ProductsGenericViewSet

router = DefaultRouter()
router.register("products",ProductsGenericViewSet, basename="products")

urlpatterns = router.urls

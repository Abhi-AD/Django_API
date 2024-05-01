from django.urls import path
from api1_app1 import views

urlpatterns = [path("api1/", views.api_home), path("api2/", views.api2_home)]

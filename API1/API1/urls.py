from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api1_app1.urls')),
    path('api/product/',include('api1_app2.urls')),
]

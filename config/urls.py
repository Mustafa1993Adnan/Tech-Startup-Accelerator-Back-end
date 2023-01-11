from django.contrib import admin
from django.urls import path
from fruit.controller import api_controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_controller.urls)
]

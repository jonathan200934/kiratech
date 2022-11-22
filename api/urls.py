from django.urls import path
from . import views

urlpatterns = [
    path('inventory', views.get_api_inventory),
    path('supplier', views.get_api_supplier),
]

from rest_framework.response import Response
from rest_framework.decorators import api_view
from inventory.models import Inventory, Supplier
from .serializers import ApiInventorySerializer, ApiSupplierSerializer


@api_view(['GET'])
def get_api_inventory(request):
    inventories = Inventory.objects.all()
    serializer = ApiInventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_api_supplier(request):
    suppliers = Supplier.objects.all()
    serializer = ApiSupplierSerializer(suppliers, many=True)
    return Response(serializer.data)

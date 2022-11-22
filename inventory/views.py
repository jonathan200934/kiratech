from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from inventory.models import Inventory
from api.serializers import InventorySerializer, ApiInventorySerializer


@api_view(['GET'])
def inventory_list(request):
    """
    Why we have to make a request to our internal api endpoint api/inventory
    when we could use models to retrieve data, simple is better than complex
    (making http request to our internal api endpoint is increasing latency)
    """
    name = request.query_params.get('name')
    if name:
        data = Inventory.objects.get(name=name)
        serializer = InventorySerializer(data)
        return Response(serializer.data)
    inventories = Inventory.objects.all()
    serializer = InventorySerializer(inventories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_specific_inventory(request, pk):
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ApiInventorySerializer(inventory)
    return Response(serializer.data)

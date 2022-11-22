from rest_framework.test import APITestCase
from rest_framework import status
from .models import Supplier, Inventory


class SimpleTestCase(APITestCase):
    def setUp(self):
        Supplier.objects.create(name="milo")
        Inventory.objects.create(name="test", description="test", supplier=Supplier.objects.first())

    def test_inventory(self):
        response = self.client.get('http://127.0.0.1/inventory')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_inventory(self):
        response = self.client.get('http://127.0.0.1/api/inventory')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_specific_inventory(self):
        response = self.client.get('http://127.0.0.1/inventory/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

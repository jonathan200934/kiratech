from django.db import models


class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    note = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey("Supplier", null=True, on_delete=models.SET_NULL)


class Supplier(models.Model):
    name = models.CharField(max_length=200)

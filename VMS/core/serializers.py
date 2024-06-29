from rest_framework import serializers
from core.models import *

class VendorSerializer(serializers.ModelSerializer):
     class Meta:
          model=Vendor
          fields='__all__'
  
class PurchaseOrderSerializer(serializers.ModelSerializer):
    Vendor=Vendor()
    class Meta:
        model = PurchaseOrder
        fields='__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    Vendor=Vendor()
    class Meta:
        model = HistoricalPerformance
        fields='__all__'
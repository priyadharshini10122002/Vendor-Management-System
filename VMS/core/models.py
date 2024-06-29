from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=50)
    contact_details=models.TextField()
    address =models.TextField()
    vendor_code=models.AutoField(primary_key=True)
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

class PurchaseOrder(models.Model):
    Vendor=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
    po_number=models.AutoField(primary_key=True)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=10)
    quality_rating =models.FloatField()
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField(null=True)

class HistoricalPerformance(models.Model) :
    vendor=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()
    
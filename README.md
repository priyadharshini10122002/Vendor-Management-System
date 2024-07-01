# Vendor-Management-System
Developing a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.


# Collection_Publishment
https://elements.getpostman.com/redirect?entityId=35061861-ee3c15f6-35f1-4d62-a643-489da5fe3207&entityType=collection

# Model Definations


# Vendor Model 
#This model stores essential information about each vendor and their performancemetrics.

● name: CharField - Vendor's name.

● contact_details: TextField - Contact information of the vendor.

● address: TextField - Physical address of the vendor.

● vendor_code: CharField - A unique identifier for the vendor.

● on_time_delivery_rate: FloatField - Tracks the percentage of on-time deliveries.

● quality_rating_avg: FloatField - Average rating of quality based on purchase orders.

● average_response_time: FloatField - Average time taken to acknowledge purchase orders.

● fulfillment_rate: FloatField - Percentage of purchase orders fulfilled successfully.





# Purchase Order (PO) Model 
#This model captures the details of each purchase order and is used to calculate various performancemetrics.

● po_number: CharField - Unique number identifying the PO.

● vendor: ForeignKey - Link to the Vendor model.

● order_date: DateTimeField - Date when the order was placed.

● delivery_date: DateTimeField - Expected or actual delivery date of the order.

● items: JSONField - Details of items ordered.

● quantity: IntegerField - Total quantity of items in the PO.

● status: CharField - Current status of the PO (e.g., pending, completed, canceled).

● quality_rating: FloatField - Rating given to the vendor for this PO (nullable).

● issue_date: DateTimeField - Timestamp when the PO was issued to the vendor.

● acknowledgment_date: DateTimeField, nullable - Timestamp when the vendor acknowledged the PO.




# Historical Performance Model 
This model optionally stores historical data on vendor performance, enabling trend analysis.

● vendor: ForeignKey - Link to the Vendor model.

● date: DateTimeField - Date of the performance record.

● on_time_delivery_rate: FloatField - Historical record of the on-time delivery rate.

● quality_rating_avg: FloatField - Historical record of the quality rating average.

● average_response_time: FloatField - Historical record of the average response time.

● fulfillment_rate: FloatField - Historical record of the fulfilment rate.


# Backend Logics
# On-Time Delivery Rate
● Logic: Count the number of completed POs delivered on or before delivery_date and divide by the total number of completed POs for that vendor.

# Quality Rating Average
● Logic: Calculate the average of all quality_rating values for completed POs ofthe vendor.

# Average Response Time
● Logic: Compute the time difference between issue_date and acknowledgment_date for each PO, and then find the average of these times for all POs of the vendor.

# Fulfilment Rate
● Logic: Divide the number of successfully fulfilled POs (status 'completed' without issues) by the total number of POs issued to the vendor.

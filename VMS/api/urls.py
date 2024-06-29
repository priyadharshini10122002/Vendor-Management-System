from core.views import *

from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
#router.register(r'vendors',VendorViewSet,basename='vendor')
#router.register(r'purchaseorders',PurchaseOrderViewSet,basename='purchaseorder')

#urlpatterns=router.urls

urlpatterns = [    
   path('',include(router.urls)),
   
   #Vendor
   path('vendors/',VendorAPI.as_view()),
   path('vendors/<int:id>/',VendorAPI.as_view()),

   #Purchase_Order
   path('purchase_orders/',PurchaseOrderAPI.as_view()),
   path('purchase_orders/<int:id>/',PurchaseOrderAPI.as_view()),

   #Perfomance
   path('vendors/<int:id>/performance/',PerformanceAPI.as_view()),


   #Acknowledgement 
   path('purchase_orders/<int:id>/acknowledge/',PurchaseOrderAPI.as_view()),
    
]
# https://documenter.getpostman.com/view/35061861/2sA3dsoEoe


##https://api.postman.com/collections/35061861-296fb6e1-d209-48fc-8f50-de41cb85eb2f?access_key=PMAT-01J1EJZ5QQM9X89WSFBFEVZ103
from django.shortcuts import render
from .models import *
from core.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from datetime import *
from django.db.models import *
from django.db.models import F
from django.db.models import F, ExpressionWrapper, DurationField


# class VendorViewSet(viewsets.ModelViewSet):
#     serializer_class=VendorSerializer
#     queryset=Vendor.objects.all()

# class PurchaseOrderViewSet(viewsets.ModelViewSet):
#     serializer_class=PurchaseOrderSerializer
#     queryset=PurchaseOrder.objects.all()

class VendorAPI(APIView):
    def get(self,request,id=None):
        if id:
            try:
               obj=Vendor.objects.get(vendor_code=id)
               serializer=VendorSerializer(obj)
               return Response(serializer.data)
            except Vendor.DoesNotExist:
                return Response({'Message : Vendor Not Exist !'})
        else:
            ob=Vendor.objects.all()
            serializer=VendorSerializer(ob,many=True)
            return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer=VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  
    def put(self,request,id):
          try:
              obj=Vendor.objects.get(vendor_code=id)
          except Vendor.DoesNotExist:
            return Response({'Message : Vendor Not Exist !'})
          serializer=VendorSerializer(obj,data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
          return Response(serializer.errors)              
    def patch(self,request,id):
          try:
              obj=Vendor.objects.get(vendor_code=id)
          except Vendor.DoesNotExist:
            return Response({'Message : Vendor Not Exist !'})
          serializer=VendorSerializer(obj,data=request.data,partial=True)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
          return Response(serializer.errors)             
    def delete(self,request,id):
        try:
            obj=Vendor.objects.get(vendor_code=id)
        except Vendor.DoesNotExist:
            return Response({'Message : Vendor Not Exist !'})
        obj.delete()
        return Response ({'The Vendor Deleted Successfully !'})







class PerformanceAPI(APIView):
    def on_time_delivery_rate(self,id):      
        com_obj=PurchaseOrder.objects.filter(Vendor=id,status='Completed').count()
        cal_obj=PurchaseOrder.objects.filter(Vendor=id,status='Completed',issue_date__lte=F('delivery_date')).count()
        val=cal_obj/com_obj
        return val
    
    def quality_rating_avg(self,id):
        t_objs=PurchaseOrder.objects.filter(Vendor=id,status='Completed').aggregate(Avg("quality_rating"))
        val= t_objs['quality_rating__avg']
        return val

    def average_response_time(self,id):
        time_difference = ExpressionWrapper(F('issue_date') - F('acknowledgment_date'), output_field=DurationField())      
        vals=PurchaseOrder.objects.filter(Vendor=id).annotate(time_difference=time_difference).aggregate(Avg("time_difference"))
        value= vals['time_difference__avg'].total_seconds()
        return (value)

    def fulfillment_rate(self,id):
        t_objs=PurchaseOrder.objects.filter(Vendor=id)
        c_objs=PurchaseOrder.objects.filter(Vendor=id,status="Completed")
        fulfillment_rate=t_objs.count()/c_objs.count()
        return (fulfillment_rate)  
    
    def insert_or_update_data(self,vals_dict,id):
        ven=Vendor.objects.get(vendor_code=id)
        obj, created = HistoricalPerformance.objects.update_or_create(vendor=id,
        defaults={
                    'vendor': ven,
                    'date':datetime.now(),
                    'on_time_delivery_rate': vals_dict['On Time Delivery Rate'],
                    'quality_rating_avg': vals_dict['Quality Average Rating'],
                    'average_response_time': vals_dict['Average Response Time'],
                    'fulfillment_rate': vals_dict['Fulfilment_Rate'] }  )
        if created:
            print("A new record was created.")
        else:
            print("An existing record was updated.")


    def get(self,request,id):    
        if id:           
            print(id)
            try:
            
               on_time_delivery_rate=self.on_time_delivery_rate(id)
               print("On Time Delivery Rate :" +str(on_time_delivery_rate))             
               quality_avg_rat=self.quality_rating_avg(id)
               print("Quality Average Rating :" +str(quality_avg_rat))
               avg_response_time=self.average_response_time(id)
               print("Average Response Time :" +str(avg_response_time))
               fulfilment_rate=self.fulfillment_rate(id)
               print("fulfilment_rate :" + str(fulfilment_rate))

               vals_dict={
                   'On Time Delivery Rate':on_time_delivery_rate,
                   'Quality Average Rating':quality_avg_rat,
                   'Average Response Time':avg_response_time,
                   'Fulfilment_Rate':fulfilment_rate
               }
               context = {'Metics':vals_dict}
        
               self.insert_or_update_data(vals_dict,id) 
               
               return Response(context)
             
            except HistoricalPerformance.DoesNotExist:
                return Response({'Message : Perfomance Not Exist !'})
        else:
            ob=HistoricalPerformance.objects.all()
            serializer=PurchaseOrderSerializer(ob,many=True)
            return Response(serializer.data)
    




class PurchaseOrderAPI(APIView):
    def post(self,request,id=None):    
      if id:
       try:
        data=request.data
        obj=PurchaseOrder.objects.get(po_number=id)
        serializer=PurchaseOrderSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()

           # self.average_response_time(id)
            
            return Response(serializer.data) 
       except PurchaseOrder.DoesNotExist:
            return Response(serializer.errors)  
      
      else:
        #return Response({'Vendor id Missing !'})
        data = request.data
        serializer=PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  

    def get(self,request,id=None):
        if id:
            try:
               obj=PurchaseOrder.objects.get(po_number=id)
               serializer=PurchaseOrderSerializer(obj)
               return Response(serializer.data)
            except PurchaseOrder.DoesNotExist:
                return Response({'Message : Purchase Order Not Exist !'})
        else:
            ob=PurchaseOrder.objects.all()
            serializer=PurchaseOrderSerializer(ob,many=True)
            return Response(serializer.data)
    
    def put(self,request,id):
          try:
              obj=PurchaseOrder.objects.get(po_number=id)
          except PurchaseOrder.DoesNotExist:
            return Response({'Message : Purchase Order Not Exist !'})
          serializer=PurchaseOrderSerializer(obj,data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
          return Response(serializer.errors)    
                           
    def delete(self,request,id):
        try:
            obj=PurchaseOrder.objects.get(po_number=id)
        except PurchaseOrder.DoesNotExist:
            return Response({'Message : Purchase Order  Not Exist !'})
        obj.delete()
        return Response ({'The Purchase Order Deleted Successfully !'})







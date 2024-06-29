


















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
        return Response({'Vendor id Missing !'})
        







##Ideas##





















































































   



        # aaggregate(difference('issue_date')-F('acknowledgment_date'))
        # print(vals)

       # print(t_objs.exists())
        #print(type(vals))
        #print(sum(vals))
        i=0
        sum_d = datetime(1,1,1,0,0)
        v=[]
        while i < len(vals):
           iss_date=vals[i].issue_date
           print(iss_date)
           ack_date=vals[i].acknowledgment_date
           print(ack_date)
           diff=ack_date-iss_date
           sum_d+=diff
           print(diff)
           v.append(diff)
           i+=1
       # print(sum_d)
        #avr=sum(v)
        return((sum_d))
    

       #Book.objects.filter(name__startswith="Django").aggregate(Avg("price"))
       
       
       
       # print(t_objs.exists())
        vals = PurchaseOrder.objects.filter(Vendor=id,status='Completed').values('quality_rating')
       # print(type(vals))
        #print(sum(vals))
        i=0
        v=[]
        while i< len(vals):
           v.append(vals[i]['quality_rating'])
           i+=1

        qra=sum(v)
        return(qra)
    

        #for i in vals:
        #   print(vals[i])

        #qr=PurchaseOrder.objects.get(Vendor=id,)
        #qr= t_objs.objects.get(['quality_rating'])
        #print(qr)

        #ratings=[]
        #for i in t_objs:
        #    print(i)

        #    for j in i:
        #      ratings.append(j['quality_rating'] )
        #qra=sum(ratings)/len(t_objs)
        #print(qra)
        #return (qra)

        #serializer=PurchaseOrderSerializer(objs,many=True)
        #print(len(objs))
        #counter=0
        #if serializer['status'] == 'Completed':
        #    counter+=1
        #    return counter
        #qra=counter/len(objs)
        #print(qra)


        #for i in objs:
        #  for ins in i: 
        #   if ins['status'] =='Completed' :
        #       counter+=1
        #  return counter
        
        #qra=counter/len(objs)
        #print(qra)
        
        
        return Response('done')

























      #  highly_rated = Count("vendor", filter=Q(book__rating__gte=7))
   #     print(c_obj)
        #objs=PurchaseOrder.objects.filter(Vendor=id,issue_date_lte = delivery_date)     
        #print(objs)
      #  val=c_obj.filter('issue_date'<'delivery_data')
      #  print(val)

        counter=0
        for i in c_obj :
           if i[8]<i[3]:
              counter +=1
        print(counter)
        #otd=counter/objs
        print (otd)
        return(otd)
#        serializer=PurchaseOrderSerializer(obj)
#        return Response(serializer.data)

        serializer=PurchaseOrderSerializer(objs)
        return Response(serializer.data)
       # for i in objs:
       #     print(objs[i])

        #obj=PurchaseOrder.objects.get(po_number=id)
     
        counter=0
        if serializer.data['status'] =='Completed' and serializer.data['issue_date']<serializer.data['delivery_date']:
            counter+=1
        




        return Response(serializer.data)
        #print(obj['Vendor','po_number','order_date'])

       # serializer=HistoricalPerformanceSerializer(obj)
      #  return Response(serializer.obj)
       # return Response('done')
    







       
   

        return Response('done')
    
    

        #print("type : "+str(type(objs)))
        serializer=PurchaseOrderSerializer(objs,many=True)
#        print(serializer.data[0])
#        print("length : "+ str(len(objs)))
#        counter=0
#        for i in serializer:
#                if i.serializer.data[0] ['status']== 'Completed':
#                    counter+=1
#        print('counter value')
#        print("Counter :" + str(counter))
        














 data=vals_dict
               obj=HistoricalPerformance.objects.get(vendor=id)
               serializer=HistoricalPerformanceSerializer(obj,data=data)
               if serializer.is_valid():
                   print("Hemllp")
                   serializer.save()
                   return Response(serializer.data)
               

        #        data=request.data
        # obj=PurchaseOrder.objects.get(po_number=id)
        # serializer=PurchaseOrderSerializer(obj,data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #    # self.average_response_time(id)
        #     return Response(serializer.data) 
        
from services.models import Services
from category.models import Category
from sub_category.models import Sub_category
from cities.models import Cities
from get_details.serializers import Get_detailsSerializer
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)

from django.views import generic
from django.views.generic import ListView

class CustomListView(ListView):
    #paginate_by = 2
    def get(self, request, *args, **kwargs):
      # service_id = request.GET.get('service_id')

      # import sys
      # print >> sys.stderr, service_id

      # error=[]

      # if(User_register.objects.filter(token_generated=access_token).exists()):
      #   pass
      # else:
      #   error.append(
      #             {
      #               'status':401,
      #               'message':"Access Token not valid"
      #             }
      #       )
      #   return JsonResponse(error[0],safe=False)



   

      #vz_id = self.kwargs['vz_id']
      sub_category_id = self.kwargs['id']

      import sys
      # print >> sys.stderr, service_id
         
      sub_category_details= Sub_category.objects.filter(id=sub_category_id)
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      # print >> sys.stderr, objects
      sub_category=[]

      for s in sub_category_details:
        c=Category.objects.get(id=s.category_id)
        service_obj=Services.objects.get(id=c.service_id)
     
        # service=list(Services.objects.filter(id=service_id))
        sub_category.append(
                  { 
                   'id': s.id,
                   'name': s.sub_category,
                   # 'description': s.description,
                   'category':c.category,
                   'service':service_obj.service,
                   'price':s.price,   
                   }
                )
        



      
      return JsonResponse(sub_category,safe=False)
  
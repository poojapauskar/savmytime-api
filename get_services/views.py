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
     

      import sys
      # print >> sys.stderr, service_id
      id1=self.kwargs['city_id']
      objects=list(Cities.objects.filter(id=id1).values_list('service_list'))
      # print >> sys.stderr, objects

      objects2=str(objects).replace('["','').replace('"]','').replace(',','').replace('[','').replace(']','').replace("'",'').replace('(','').replace(')','')
      
      # print >> sys.stderr, "objects2"

      objects2= objects2.split()
      # objects2=objects2.replace('[','')
      print >> sys.stderr, objects2

      import json

      # objects3=[86, 87,];
      # print >> sys.stderr, "objects3"
      # print >> sys.stderr, objects3

      # import json
      services=list(Services.objects.filter(id__in=objects2).values('service','id','description','image','icon'))

      # list1=Services.objects.filter(id__in=(objects2)).values('service','id')
      # print list1.query
      print >> sys.stderr, services






      # services= list(Services.objects.all().values('service','id','description','image'))
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      # print >> sys.stderr, objects

      
      return JsonResponse(services,safe=False)
  
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
      
        
      cities= list(Cities.objects.all().values('city','id','service_list'))
      #tickets = Ticket.objects.filter(vz_id__in=contacts)
      # print >> sys.stderr, objects


      #Services.objects.filter(service="Painting").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id607797.png")
      #Services.objects.filter(service="Painting").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id837972.png")

      #Services.objects.filter(service="Plumbing").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id523993.png")
      #Services.objects.filter(service="Plumbing").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id134922.png")

      #Services.objects.filter(service="Carpenter").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id317696.png")
      #Services.objects.filter(service="Carpenter").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id748457.png")

      #Services.objects.filter(service="Electrician").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id796318.png")
      #Services.objects.filter(service="Electrician").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id692779.png")

      #Services.objects.filter(service="C A Consult").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id155895.png")
      #Services.objects.filter(service="C A Consult").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id851553.png")


      #Services.objects.filter(service="AC Repair").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id232500.png")
      #Services.objects.filter(service="AC Repair").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id103130.png")

      #Services.objects.filter(service="Pest control").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id822384.png")
      #Services.objects.filter(service="Pest control").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id800524.png")

      #Services.objects.filter(service="Security Solutions").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id117663.png")
      #Services.objects.filter(service="Security Solutions").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id208276.png")


      #Services.objects.filter(service="Graphic Design").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id322845.png")
      #Services.objects.filter(service="Graphic Design").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id968958.png")


      #Services.objects.filter(service="Digital Marketing").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id684436.png")
      #Services.objects.filter(service="Digital Marketing").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id190946.png")


      #Services.objects.filter(service="Chartered Prop Care").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id679993.png")
      #Services.objects.filter(service="Chartered Prop Care").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id818583.png")


      #Services.objects.filter(service="Laptop Servicing").update(icon="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id740750.png")
      #Services.objects.filter(service="Laptop Servicing").update(image="http://res.cloudinary.com/htwoqvwuz/image/upload/savmytime/id393276.png")

      
      return JsonResponse(cities,safe=False)
  
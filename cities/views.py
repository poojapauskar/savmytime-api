from cities.models import Cities
from cities.serializers import CitiesSerializer
from rest_framework import generics


class CitiesList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class CitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer




# from cities.models import Cities
# from rest_framework import generics
# # from ticket.permissions import IsOwnerOrReadOnly
# # from rest_framework import permissions
# from django.shortcuts import get_object_or_404

# from rest_framework.views import APIView

# class edit_cityList(APIView):
#  def put(self, request, format=None):
#   Cities.objects.filter(id=request.data['id']).update(city=request.data['city'],service_list=request.data['list'])
#     #   return validated_data
#   details=[]
#   details.append(
#                   {
#                    'status':200,
#                    'message':'Updated',
#                   }
#                  )  

#   import sys
#   from django.http import JsonResponse
#   return JsonResponse(details[0],safe=False)

# from django.http import JsonResponse

# class StatusCode(object):
#     OK = 200
#     NOT_FOUND = 404
#     # add more status code according to your need
# import json
# from django.http import HttpResponse
 
# def JSONResponse(data = None, status = StatusCode.OK):
#     if data is None:
#         return HttpResponse(status)
#     if data and type(data) is dict:
#         return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
#             mimetype = 'application/json', status = status)
#     else:
#         return HttpResponse(status = StatusCode.NOT_FOUND)
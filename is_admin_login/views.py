from user_data.models import User_data
# from login.serializers import LoginSerializer
from rest_framework import generics

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

class Is_admin_loginList(generics.ListCreateAPIView):
 def get(self, request, *args, **kwargs):
  object1=request.META.get('HTTP_EMAIL')
  details=[]

  import sys
  print >> sys.stderr, request.META.get('HTTP_EMAIL')          
  if(User_data.objects.filter(email=request.META.get('HTTP_EMAIL')).exists()):
   if(User_data.objects.filter(email=request.META.get('HTTP_EMAIL'),password=request.META.get('HTTP_PASSWORD')).exists()):
    details.append(
                  {
                   'status':200,
                   'message':'Is Admin',
                  }
                 )
   else:
    details.append(
                  {
                   'status':401,
                   'message':'Password invalid',
                  }
                 )  
  else:
   details.append(
                  {
                   'status':400,
                   'message':'Admin does not exists',
                  }
                 )  

  import sys
  from django.http import JsonResponse
  return JsonResponse(details[0],safe=False)
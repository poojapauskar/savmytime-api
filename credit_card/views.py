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
 def get(self, request, *args, **kwargs):

  # in headers CREDIT-CARD-NO
  import sys
  credit_card_no= request.META.get('HTTP_CREDIT_CARD_NO')
  amount= request.META.get('HTTP_AMOUNT')
  expiry_date= request.META.get('HTTP_EXPIRY_DATE')

  # print sys.stderr, "credit_card_no"
  # print sys.stderr, credit_card_no
  # print sys.stderr, "amount"
  # print sys.stderr, amount
  # print sys.stderr, "expiry_date"
  # print sys.stderr, expiry_date

  # credit_card_no= "4111111111111111"
  # amount= "150"
  # expiry_date= "2020-12"

  from authorizenet import apicontractsv1 
  from authorizenet.apicontrollers import *
  from decimal import *

  merchantAuth = apicontractsv1.merchantAuthenticationType()
  merchantAuth.name = '3L8QRmu497'
  merchantAuth.transactionKey = '8a92dCH8k4x4Ms53'

  creditCard = apicontractsv1.creditCardType()
  creditCard.cardNumber = credit_card_no
  # "2020-12"
  creditCard.expirationDate = expiry_date

  payment = apicontractsv1.paymentType()
  payment.creditCard = creditCard

  transactionrequest = apicontractsv1.transactionRequestType()
  transactionrequest.transactionType = "authCaptureTransaction"
  # transactionrequest.amount = Decimal ('1.55')
  transactionrequest.amount = Decimal (amount)
  transactionrequest.payment = payment


  createtransactionrequest = apicontractsv1.createTransactionRequest()
  createtransactionrequest.merchantAuthentication = merchantAuth
  createtransactionrequest.refId = "MerchantID-0001"

  createtransactionrequest.transactionRequest = transactionrequest
  createtransactioncontroller = createTransactionController(createtransactionrequest)
  createtransactioncontroller.execute()

  response = createtransactioncontroller.getresponse()

  details=[]
  if (response.messages.resultCode=="Ok"):
   print "Transaction ID : %s" % response.transactionResponse.transId
   details.append(
          {
           'status':200,
           'message':'Successful Transaction',
          }
         )
  else:
   print "response code: %s" % response.messages.resultCode
   details.append(
          {
           'status':400,
           'message':'Error',
          }
         )
  

  return JsonResponse(details,safe=False)
  
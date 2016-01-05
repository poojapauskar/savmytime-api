from services.models import Services
from services.serializers import ServicesSerializer
from rest_framework import generics


class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
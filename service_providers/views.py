from service_providers.models import Service_providers
from service_providers.serializers import Service_providersSerializer
from rest_framework import generics


class Service_providersList(generics.ListCreateAPIView):
    queryset = Service_providers.objects.all()
    serializer_class = Service_providersSerializer


class Service_providersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service_providers.objects.all()
    serializer_class = Service_providersSerializer
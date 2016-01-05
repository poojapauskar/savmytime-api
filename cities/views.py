from cities.models import Cities
from cities.serializers import CitiesSerializer
from rest_framework import generics


class CitiesList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class CitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
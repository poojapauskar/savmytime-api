from sub_category.models import Sub_category
from sub_category.serializers import Sub_categorySerializer
from rest_framework import generics


class Sub_categoryList(generics.ListCreateAPIView):
    queryset = Sub_category.objects.all()
    serializer_class = Sub_categorySerializer


class Sub_categoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sub_category.objects.all()
    serializer_class = Sub_categorySerializer
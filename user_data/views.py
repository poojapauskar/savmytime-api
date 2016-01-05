from user_data.models import User_data
from user_data.serializers import User_dataSerializer
from rest_framework import generics


class User_dataList(generics.ListCreateAPIView):
    queryset = User_data.objects.all()
    serializer_class = User_dataSerializer


class User_dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_data.objects.all()
    serializer_class = User_dataSerializer
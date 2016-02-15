from transition.models import Transition
from transition.serializers import TransitionSerializer
from rest_framework import generics


class TransitionList(generics.ListCreateAPIView):
    queryset = Transition.objects.all()
    serializer_class = TransitionSerializer


class TransitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transition.objects.all()
    serializer_class = TransitionSerializer
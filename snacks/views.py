from rest_framework import generics
from .serializer import SnackSerializer
from .models import Snack

class SnackList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(generics.RetrieveUpdateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

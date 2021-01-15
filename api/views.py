from rest_framework import generics, permissions

from dashboard.models import VeterinaryOfficer
from .serializers import VeterinaryOfficerSerializer

# Create your views here.


class VeterinaryOfficerList(generics.ListCreateAPIView):
    queryset = VeterinaryOfficer.objects.all()
    serializer_class = VeterinaryOfficerSerializer


class VeterinaryOfficerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VeterinaryOfficer.objects.all()
    serializer_class = VeterinaryOfficerSerializer

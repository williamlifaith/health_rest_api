from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from django.db.models import Avg, Max, Min, Count
from .serializers import Event_typeSerializer, PatientSerializer, EventSerializer
from .models import Event_type, Patient, Event
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# Create your views here.

# use viewsets return patient queryset
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        patient = Patient.objects.all()
        return patient


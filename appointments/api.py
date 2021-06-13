from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.decorators import api_view

class AppointmentsViewSet(viewsets.ModelViewSet):
	serializer_class  = Appointments_Serializer
	queryset          = Appointment.objects.all()
	# http_method_names = ['get']
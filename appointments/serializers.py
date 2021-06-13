from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User


# Appointments Serializer
class Appointments_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = '__all__'




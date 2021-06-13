from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User


# Cases Serializer
class Cases_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Case
		fields = '__all__'




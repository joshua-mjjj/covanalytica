from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User


# Reviews Serializer
class Reviews_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'




from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.decorators import api_view

class ReviewsViewSet(viewsets.ModelViewSet):
	serializer_class  = Reviews_Serializer
	queryset          = Review.objects.all()
	http_method_names = ['get', 'post']
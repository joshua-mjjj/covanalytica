from .models import *
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from .serializers import *
from rest_framework.decorators import api_view

class CasesViewSet(viewsets.ModelViewSet):
	serializer_class  = Cases_Serializer
	queryset          = Case.objects.all()
from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Case(models.Model):
	first_name    =  models.CharField(max_length=100, blank=False, null=False)
	last_name     =  models.CharField(max_length=100, blank=False, null=False)
	location      =  models.CharField(max_length=100, blank=False, null=False)
	contact       =  models.CharField(max_length=100, blank=False, null=False)
	guardian      =  models.CharField(max_length=100, blank=True, null=True)
	age_bracket   =  models.CharField(max_length=100, blank=False, null=False)
	status        =  models.CharField(max_length=300, blank=False, null=False)

	def __str__(self):
		return '{}'.format(self.first_name)
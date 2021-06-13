from django.db import models

# Create your models here.

class Appointment(models.Model):
	full_name     =  models.CharField(max_length=100, blank=False, null=False)
	location      =  models.CharField(max_length=100, blank=False, null=False)
	sickness      =  models.CharField(max_length=100, blank=False, null=False)
	contact       =  models.CharField(max_length=100, blank=False, null=False)
	guardian      =  models.CharField(max_length=100, blank=True,  null=True)
	doctor        =  models.CharField(max_length=100, blank=False, null=False)
	status        =  models.CharField(max_length=300, blank=False, null=False)

	def __str__(self):
		return '{}'.format(self.full_name)
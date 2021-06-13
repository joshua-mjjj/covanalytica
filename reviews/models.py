from django.db import models

# Create your models here.

class Review(models.Model):
	first_name    =  models.CharField(max_length=100, blank=False, null=False)
	last_name     =  models.CharField(max_length=100, blank=False, null=False)
	comment       =  models.CharField(max_length=500, blank=False, null=False)
	contact       =  models.CharField(max_length=100, blank=True,  null=True)
	photo         =  models.FileField(upload_to="media/avatars/", blank=False)

	def __str__(self):
		return '{}'.format(self.first_name)
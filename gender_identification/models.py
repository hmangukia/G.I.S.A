from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
	text = models.TextField(help_text='Enter the data which you want to analyse')

	def __str__(self):
		return self.name

class Info(models.Model):
	text = models.TextField(help_text='Enter the data which you want to analyse')
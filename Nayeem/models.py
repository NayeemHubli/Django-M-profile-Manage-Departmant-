from django.db import models

# Create your models here.
class RegisterDetails(models.Model):
	Rname = models.CharField(max_length=40) 
	Remail = models.CharField(max_length=40,primary_key=True) 
	Rnum = models.IntegerField(10)
	password = models.CharField(max_length=10)
	Rcpass = models.CharField(max_length=10)
	Rcity = models.CharField(max_length=40)
	Redu = models.CharField(max_length=50)
	Raim = models.CharField(max_length=30)
	Rhob = models.CharField(max_length=30)
	
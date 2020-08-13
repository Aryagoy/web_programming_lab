from django.db import models





class loginform(models.Model):
    name = models.CharField(max_length=100)
    reg_no= models.CharField(max_length=100)
    dept= models.CharField(max_length=100)
    degree = models.CharField(max_length=10)

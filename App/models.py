from django.db import models
from django.contrib.auth.models import  User
# Create your models here.



class Todo(models.Model):
    tital = models.CharField(max_length=20)
    descripation = models.CharField(max_length=100)
    date = models.DateField()

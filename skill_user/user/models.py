from django.db import models

# Create your models here.

class User(models.Model):
    website = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

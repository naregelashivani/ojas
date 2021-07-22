from django.db import models

# Create your models here.
class Data(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField(max_length=40)
    Contact=models.IntegerField()
    Messages=models.CharField(max_length=200)

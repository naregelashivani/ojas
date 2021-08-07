from django.db import models

# Create your models here.
class Ticket_User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=80)
    startingpoint = models.CharField(max_length=80)
    endingpoint = models.CharField(max_length=80)
    date = models.DateField(max_length=80)
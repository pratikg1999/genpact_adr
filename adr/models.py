from django.db import models

# Create your models here.
class Prescription(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField()
    disease = models.CharField(max_length=100)
    medication = models.CharField(max_length=100)
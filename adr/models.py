from django.db import models

# Create your models here.
class Prescription(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField()
    disease = models.CharField(max_length=100)
    medication = models.CharField(max_length=100)

class ADRDatabase(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length = 6)
    location = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)
    medicine_category = models.IntegerField()
    label = models.DecimalField(max_digits=5, decimal_places=3)

    
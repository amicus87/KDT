from django.db import models

class hospital(models.Model):
    name = models.CharField(max_length=10)
    sep = models.CharField(max_length=10)
    tel = models.CharField(max_length=10)
    zip = models.IntegerField()
    add = models.CharField(max_length=50)

class population(models.Model):
    age=models.IntegerField()
    total=models.IntegerField()
    male=models.IntegerField()
    female=models.IntegerField()
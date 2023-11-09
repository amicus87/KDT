from django.db import models

class population(models.Model):
    age = models.IntegerField()
    total = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()

class hospital(models.Model):
    objects=models.Manager()
    name = models.CharField(max_length=20)
    type=models.CharField(null=True, max_length=10)
    type_short=models.CharField(null=True, max_length=10)
    tel=models.CharField(null=True, max_length=15)
    zip=models.IntegerField()
    add=models.CharField(max_length=50)
    place=models.CharField(max_length=10)
from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    architect = models.ManyToManyField('Architect')
    style = models.ForeignKey('Style', on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Architect(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Style(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Create your models here.

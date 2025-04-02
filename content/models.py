from django.db import models

class Architect(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Style(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    architects = models.ManyToManyField(Architect, related_name='buildings')
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='buildings')
    year = models.IntegerField()

    def __str__(self):
        return self.name
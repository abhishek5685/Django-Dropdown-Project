from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
       return self.name

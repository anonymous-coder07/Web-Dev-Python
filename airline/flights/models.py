from django.db import models

# Create your models here.
class Airports(models.Model):
    code = models.CharField(max_length = 64)
    city = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.city}: ({self.code})"

class Flight(models.Model):

    origin = models.ForeignKey(Airports, on_delete = models.CASCADE, related_name = 'departures')
    destination = models.ForeignKey(Airports, on_delete = models.CASCADE, related_name = 'arrivals')
    duration = models.IntegerField()
    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination}'
    
class Passengers(models.Model):
    firstname = models.CharField(max_length = 64)
    secondname = models.CharField(max_length = 64)
    flights = models.ManyToManyField(Flight, blank= True, related_name= 'passengers')
    def __str__(self):
        return f'First Name: {self.firstname} Second Name: {self.secondname}'
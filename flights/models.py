from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length= 3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return (f'{self.id}: {self.origin} to {self.destination} lasting {self.duration} minutes')

class passenger(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.firstName} ({self.lastName})"

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(null=False, max_length=200, default='')

    def __str__(self):
        return "Name: " + self.name + ", Description: " + self.description


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='')
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('MINIVAN', 'Minivan'),
        ('PICKUP', 'Pickup'),
    ]
    type = models.CharField(
        null=False, max_length=15, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        null=False, default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)])

    def __str__(self):
        return "Name: " + self.name + ", Type: " + self.type + \
               ", Year: " + str(self.year)

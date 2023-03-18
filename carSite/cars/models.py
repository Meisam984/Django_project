from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"The car is of brand {self.brand} manufactured in {self.year}"
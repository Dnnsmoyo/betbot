from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=1000)
    position = models.CharField(max_length=1000)
    contact = models.EmailField(max_length=1000)
    age = models.IntegerField()
    address = models.CharField(max_length=1000)
    salary = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return f"{self.slug}"

class Car(models.Model):
    name = models.CharField(max_length=1000)
    year = models.IntegerField(max_length=1000)
    date_purchased = models.DateField(max_length=1000)
    milleage = models.IntegerField()
    color = models.CharField(max_length=1000)
    maintanance = models.CharField(max_length=1000)
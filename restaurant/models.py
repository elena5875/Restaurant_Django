#models.py
# models.py

from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    num_guests = models.PositiveIntegerField()

    # Add any other fields you need for the reservation

    def __str__(self):
        return f'Reservation for {self.user.username} at {self.date_time}'



class Reservation(models.Model):
    # Define fields for your reservation model
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    # Add more fields as needed

    def __str__(self):
        return self.name

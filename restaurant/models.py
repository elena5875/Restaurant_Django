# models.py

from django.db import models
from django.utils import timezone

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)  # Automatically set the date to the current date
    time = models.TimeField(choices=[(timezone.datetime.strptime(f'{hour}:00', '%H:%M').time(), f'{hour}:00 PM') for hour in range(17, 24)])  # Limit time choices from 5pm to 11pm
    number_of_people = models.IntegerField(choices=[(i, i) for i in range(1, 10)], default=1)  # Limit number of people from 1 to 9
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.name

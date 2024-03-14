# models.py

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


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
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    date = models.DateField()
    time = models.TimeField(choices=[(f'{hour}:00', f'{hour}:00 PM') for hour in range(17, 24)], validators=[RegexValidator(regex=r'^([1][7-9]|20|21|22|23):00$', message="Time must be between 5:00 PM and 11:00 PM")])
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"


#models.py
from django.db import models

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Adjust max_length as needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.id} - {self.date} {self.time}"

class Review(models.Model):
    email = models.EmailField()
    review_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


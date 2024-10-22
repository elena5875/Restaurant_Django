from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Reservation(models.Model):
    """
    Model representing a table reservation at the restaurant.

    Attributes:
        PENDING (str): Status indicating the reservation is pending.
        CONFIRMED (str): Status indicating the reservation is confirmed.
        CANCELED (str): Status indicating the reservation is canceled.
        STATUS_CHOICES (list): A list of tuples representing valid status options for reservations.
        
    Fields:
        name (str): The name of the person making the reservation.
        email (str): The email address of the person making the reservation.
        phone_number (str): The phone number of the person making the reservation.
        date (date): The date of the reservation.
        time (time): The time of the reservation.
        number_of_people (int): The number of people for the reservation, limited to 1-9.
        status (str): The current status of the reservation, default is 'pending'.
    """
    
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
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        """Return a string representation of the reservation."""
        return f"{self.name} - {self.date} at {self.time}"


class Review(models.Model):
    """
    Model representing a review submitted by a customer.

    Attributes:
        name (str): The name of the person submitting the review.
        email (str): The email address of the person submitting the review.
        review_text (str): The text of the review.
        is_approved (bool): Status indicating if the review is approved (default is False).
        is_posted (bool): Status indicating if the review is publicly posted (default is False).
        created_at (datetime): The timestamp when the review was created.
    """
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    review_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)  # Add this field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the review."""
        return self.name


class Comment(models.Model):
    """
    Model representing a comment on a review.

    Attributes:
        review (ForeignKey): The review that this comment is associated with.
        comment_text (str): The text of the comment.
        created_at (datetime): The timestamp when the comment was created.
    """
    
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the comment."""
        return f'Comment on {self.review.name}'
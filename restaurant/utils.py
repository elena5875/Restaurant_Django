from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Review

def send_reservation_confirmation_email(reservation):
    """
    Send a confirmation email for a reservation.

    Args:
        reservation (Reservation): The reservation object containing details
        needed for the confirmation email.
    """
    subject = 'Reservation Approved'  # Subject of the email
    # Render the HTML template for the email body using the reservation details
    html_message = render_to_string('reservation_approved_email.html', {
        'reservation': reservation
    })
    # Strip HTML tags to create a plain text version of the email
    plain_message = strip_tags(html_message)
    # Send the email using Django's send_mail function
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,  # From email address configured in settings
        [reservation.email],  # To email address
        html_message=html_message  # HTML message content
    )

def send_reservation_cancellation_email(reservation):
    """
    Send a cancellation email for a reservation.

    Args:
        reservation (Reservation): The reservation object containing details
        needed for the cancellation email.
    """
    subject = 'Reservation Rejected'  # Subject of the email
    # Render the HTML template for the email body using the reservation details
    html_message = render_to_string('reservation_rejected_email.html', {
        'reservation': reservation
    })
    # Strip HTML tags to create a plain text version of the email
    plain_message = strip_tags(html_message)
    # Send the email using Django's send_mail function
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,  # From email address configured in settings
        [reservation.email],  # To email address
        html_message=html_message  # HTML message content
    )

def reject_review(modeladmin, request, queryset):
    """
    Reject selected reviews and send rejection emails.

    Args:
        modeladmin: The model admin that called this action.
        request: The HTTP request object.
        queryset: The queryset of reviews to be rejected.
    """
    for review in queryset:
        review.send_rejection_email()  # Send a rejection email for each review
        review.delete()  # Delete the review from the database

# Short description for the admin action
reject_review.short_description = "Reject selected reviews and send rejection emails"

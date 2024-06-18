# restaurant/utils.py

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Review

def send_reservation_confirmation_email(reservation):
    subject = 'Reservation Approved'
    html_message = render_to_string('reservation_approved_email.html', {
        'reservation': reservation
    })
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [reservation.email], html_message=html_message)

def send_reservation_cancellation_email(reservation):
    subject = 'Reservation Rejected'
    html_message = render_to_string('reservation_rejected_email.html', {
        'reservation': reservation
    })
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [reservation.email], html_message=html_message)

def reject_review(modeladmin, request, queryset):
    for review in queryset:
        review.send_rejection_email()
        review.delete()

reject_review.short_description = "Reject selected reviews and send rejection emails"

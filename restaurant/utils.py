from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Review

def send_reservation_confirmation_email(email, date, time, people):
    subject = 'Reservation Confirmation'
    html_message = render_to_string('reservation_confirmation_email.html',
                                    {'date': date, 'time': time, 'people': people})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [email], html_message=html_message)

def send_reservation_cancellation_email(email):
    subject = 'Reservation Cancellation'
    html_message = render_to_string('reservation_cancellation_email.html')
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [email], html_message=html_message)

def reject_review(modeladmin, request, queryset):
    for review in queryset:
        review.send_rejection_email()
        review.delete()

reject_review.short_description = "Reject selected reviews and send rejection emails"

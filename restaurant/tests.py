# tests.py
from django.core import mail
from django.test import TestCase
from django.utils import timezone
from .models import Reservation  # Assuming you have a Reservation model
from .utils import (
    send_reservation_confirmation_email,
    send_reservation_cancellation_email
)
from mainproject.settings import DATABASES



# Your test cases here

class EmailSendingTestCase(TestCase):
    def test_reservation_confirmation_email(self):
        # Create a test reservation
        reservation = Reservation.objects.create(
            date=timezone.now().date(),
            time=timezone.now().time(),
            people=4,
            email='test@example.com'
        )

        # Send reservation confirmation email
        send_reservation_confirmation_email(reservation.email, reservation.date, reservation.time, reservation.people)

        # Check that one message has been sent
        self.assertEqual(len(mail.outbox), 1)

        # Verify the email contents
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Reservation Confirmation')
        self.assertInHTML(f'<p>Date: {reservation.date}</p>', email.body)
        self.assertInHTML(f'<p>Time: {reservation.time}</p>', email.body)
        self.assertInHTML(f'<p>Number of People: {reservation.people}</p>', email.body)

    def test_reservation_cancellation_email(self):
        # Create a test reservation
        reservation = Reservation.objects.create(
            date=timezone.now().date(),
            time=timezone.now().time(),
            people=4,
            email='test@example.com'
        )

        # Send reservation cancellation email
        send_reservation_cancellation_email(reservation.email)

        # Check that one message has been sent
        self.assertEqual(len(mail.outbox), 1)

        # Verify the email contents
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Reservation Cancellation')
        # Add additional checks for email body/content if needed

    # Override the database user for tests
    DATABASES['default']['USER'] = 'test_database_user'
    DATABASES['default']['PASSWORD'] = 'test_database_password'
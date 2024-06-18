#from django.test import TestCase
from django.test import TestCase, Client  
from django.core import mail
from django.urls import reverse
from .models import Reservation, Review, Comment
from .utils import send_reservation_confirmation_email, send_reservation_cancellation_email
from .forms import ReviewForm, CommentForm
from .models import Review, Comment

class EmailSendingTestCase(TestCase):
    def test_reservation_confirmation_email(self):
        # Create a reservation
        reservation = Reservation.objects.create(
            name='John Doe',
            email='john@example.com',
            phone_number='+1234567890',
            date='2024-06-20',
            time='18:00:00',
            number_of_people=4,
            status='pending'
        )
        
        # Simulate sending a confirmation email
        reservation.status = 'confirmed'
        reservation.save()

        # Send the email
        send_reservation_confirmation_email(reservation)
        
        # Check that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        
        # Verify the subject and body of the email
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Reservation Approved')
        self.assertIn('Your reservation for', email.body)

    def test_reservation_cancellation_email(self):
        # Create a reservation
        reservation = Reservation.objects.create(
            name='Jane Doe',
            email='jane@example.com',
            phone_number='+1234567891',
            date='2024-06-21',
            time='19:00:00',
            number_of_people=2,
            status='pending'
        )
        
        # Simulate sending a cancellation email
        reservation.status = 'canceled'
        reservation.save()

        # Send the email
        send_reservation_cancellation_email(reservation)
        
        # Check that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        
        # Verify the subject and body of the email
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Reservation Rejected')
        self.assertIn('Your reservation for', email.body)



class ReviewViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.review1 = Review.objects.create(name='John Doe', email='john@example.com', review_text='Great place!', is_approved=True)
        self.review2 = Review.objects.create(name='Jane Smith', email='jane@example.com', review_text='Not bad.', is_approved=False)
        self.review3 = Review.objects.create(name='Alice Johnson', email='alice@example.com', review_text='Would visit again.', is_approved=True)

    def test_review_list(self):
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')
        reviews = list(response.context['reviews'])
        self.assertEqual(reviews, [self.review3, self.review1])  # Ordered by created_at desc

    def test_review_create_get(self):
        response = self.client.get(reverse('review_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_form.html')
        self.assertIsInstance(response.context['form'], ReviewForm)

    def test_review_create_post(self):
        form_data = {'name': 'Bob Brown', 'email': 'bob@example.com', 'review_text': 'Fantastic!'}
        response = self.client.post(reverse('review_create'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect to review_list
        self.assertTrue(Review.objects.filter(name='Bob Brown', email='bob@example.com').exists())

    def test_review_create_post_invalid(self):
        form_data = {'name': '', 'email': 'bob@example.com', 'review_text': 'Fantastic!'}  # Invalid name
        response = self.client.post(reverse('review_create'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_form.html')
        self.assertFalse(Review.objects.filter(email='bob@example.com').exists())

    # Print the response content for debugging
        print(response.content.decode('utf-8'))

        self.assertContains(response, 'There was an error with your submission. Please correct the errors below.')




    def test_review_detail_get(self):
        response = self.client.get(reverse('review_detail', args=[self.review1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_detail.html')
        self.assertEqual(response.context['review'], self.review1)
        self.assertIsInstance(response.context['form'], CommentForm)

    def test_review_detail_post(self):
        form_data = {'comment_text': 'Nice review!'}
        response = self.client.post(reverse('review_detail', args=[self.review1.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect to review_detail
        self.assertTrue(Comment.objects.filter(review=self.review1, comment_text='Nice review!').exists())

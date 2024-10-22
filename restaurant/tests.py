from django.test import TestCase, Client  
from django.core import mail
from django.urls import reverse
from .models import Reservation, Review, Comment
from .utils import send_reservation_confirmation_email, send_reservation_cancellation_email
from .forms import ReviewForm, CommentForm


class EmailSendingTestCase(TestCase):
    """
    Test case for verifying email sending functionality related to reservations.

    This class contains tests for sending confirmation and cancellation emails
    when a reservation's status is updated.
    """

    def test_reservation_confirmation_email(self):
        """
        Test that a confirmation email is sent when a reservation is confirmed.

        This test creates a reservation, changes its status to 'confirmed',
        and verifies that the correct email is sent with the expected subject
        and content.
        """
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
        """
        Test that a cancellation email is sent when a reservation is canceled.

        This test creates a reservation, changes its status to 'canceled',
        and verifies that the correct email is sent with the expected subject
        and content.
        """
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
    """
    Test case for verifying the views related to reviews.

    This class contains tests for listing, creating, and retrieving reviews
    in the application.
    """

    def setUp(self):
        """
        Set up test data for the review tests.

        This method creates a client instance and pre-populates the database
        with sample reviews for testing purposes.
        """
        self.client = Client()
        self.review1 = Review.objects.create(name='John Doe', email='john@example.com', review_text='Great place!', is_approved=True)
        self.review2 = Review.objects.create(name='Jane Smith', email='jane@example.com', review_text='Not bad.', is_approved=False)
        self.review3 = Review.objects.create(name='Alice Johnson', email='alice@example.com', review_text='Would visit again.', is_approved=True)

    def test_review_list(self):
        """
        Test that the review list view returns the correct response and template.

        This test checks that the review list view returns a 200 status code,
        uses the correct template, and displays the correct reviews in the context.
        """
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')
        reviews = list(response.context['reviews'])
        self.assertEqual(reviews, [self.review3, self.review1])  # Ordered by created_at desc

    def test_review_create_get(self):
        """
        Test that the review creation view returns the correct response and form.

        This test checks that the review create view returns a 200 status code,
        uses the correct template, and includes a valid form in the context.
        """
        response = self.client.get(reverse('review_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_form.html')
        self.assertIsInstance(response.context['form'], ReviewForm)

    def test_review_create_post(self):
        """
        Test that a review can be created successfully via POST request.

        This test checks that submitting valid review data creates a new review
        and redirects to the review list.
        """
        form_data = {'name': 'Bob Brown', 'email': 'bob@example.com', 'review_text': 'Fantastic!'}
        response = self.client.post(reverse('review_create'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect to review_list
        self.assertTrue(Review.objects.filter(name='Bob Brown', email='bob@example.com').exists())

    def test_review_create_post_invalid(self):
        """
        Test that submitting invalid review data returns the correct response.

        This test checks that when invalid data is submitted, the form is re-displayed
        with the appropriate error messages, and no new review is created.
        """
        form_data = {'name': '', 'email': 'bob@example.com', 'review_text': 'Fantastic!'}  # Invalid name
        response = self.client.post(reverse('review_create'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_form.html')
        self.assertFalse(Review.objects.filter(email='bob@example.com').exists())

        # Print the response content for debugging
        print(response.content.decode('utf-8'))

        self.assertContains(response, 'This field is required.')

    def test_review_detail_get(self):
        """
        Test that the review detail view returns the correct response and review.

        This test checks that accessing a specific review returns a 200 status code,
        uses the correct template, and includes the right review and comment form in context.
        """
        response = self.client.get(reverse('review_detail', args=[self.review1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_detail.html')
        self.assertEqual(response.context['review'], self.review1)
        self.assertIsInstance(response.context['form'], CommentForm)

    def test_review_detail_post(self):
        """
        Test that a comment can be added to a review via POST request.

        This test checks that submitting a valid comment on a review redirects to
        the review detail page and creates the comment successfully.
        """
        form_data = {'comment_text': 'Nice review!'}
        response = self.client.post(reverse('review_detail', args=[self.review1.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)  # Should redirect to review_detail
        self.assertTrue(Comment.objects.filter(review=self.review1, comment_text='Nice review!').exists())

from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class ReservationFormTest(TestCase):
    def test_reservation_form_submission(self):
        # Prepare form data
        form_data = {
            'date': '2024-03-10',
            'time': '18:00',
            'people': '4',
            'email': 'test@example.com',
            'phone': '123-456-7890'
        }

        # Submit the form
        response = self.client.post(reverse('reservation'), form_data)

        # Check if the form submission was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the confirmation message is present in the response content
        self.assertContains(response, 'Reservation successful!')
        
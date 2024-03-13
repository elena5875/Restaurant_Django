#Views.py

import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Reservation, Review
from .forms import ReviewForm
from .utils import send_reservation_confirmation_email, send_reservation_cancellation_email


def home(request):
    return render(request, 'home.html')


def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})



def your_reservation_view(request):
    # Your view logic goes here
    # Render the reservation template
    response = render(request, 'reservation.html')
    # Set the Content-Security-Policy header in the response
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval';"
    return response


def reservation_view(request):
    if request.method == 'POST':
        # Extract form data
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Log the form data
        logging.info("Received form data:")
        logging.info("Date: %s", date)
        logging.info("Time: %s", time)
        logging.info("Number of People: %s", people)
        logging.info("Email: %s", email)
        logging.info("Phone: %s", phone)

        # Perform server-side validation
        if not (date and time and people and email and phone):
            return HttpResponse('All fields are required.', status=400)

        # Create a new Reservation object and save it to the database
        reservation = Reservation.objects.create(date=date, time=time, number_of_people=people, email=email,
                                                 phone_number=phone)

        # Send email to the user
        send_mail(
            'Reservation Confirmation',
            f'Thank you for your reservation!\n\nHere are your reservation details:\n\nDate: {date}\nTime: {time}\nNumber of People: {people}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        # Optionally, send email notification to the admin
        send_mail(
            'New Reservation',
            f'A new reservation has been made.\n\nReservation Details:\n\nDate: {date}\nTime: {time}\nNumber of People: {people}\nEmail: {email}\nPhone: {phone}',
            settings.ADMIN_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Redirect to a thank you page or any other page
        return HttpResponse('Reservation successfully made! Thank you.')

    return render(request, 'reservation.html', {'hours_range': range(17, 24), 'people_range': range(1, 10)})



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

def reviews(request):
    # Retrieve approved reviews from the database
    approved_reviews = Review.objects.filter(approved=True)
    return render(request, 'reviews.html', {'reviews': approved_reviews})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            # Optionally, send email notification to the admin
            send_mail(
                'New Review',
                f'A new review titled "{review.title}" has been submitted.',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            # Redirect to the reviews page after submission
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})

def reject_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    # Mark the review as rejected
    review.rejected = True
    review.save()
    # Mock email for review rejection
    send_mail(
        'Review Rejection Notification',
        f'Your review titled "{review.title}" has been rejected.',
        settings.DEFAULT_FROM_EMAIL,
        [review.submitted_by],
        fail_silently=False,
    )
    # Redirect to an appropriate page
    return redirect('admin_dashboard')

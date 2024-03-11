# views.py
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Reservation, Review
from .forms import ReviewForm

# Create your views here.

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # Redirect to the reviews page after submission
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def home(request):
    return render(request, 'home.html')


def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})


# View for handling reservation form submission
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
            settings.elenafreire75@gmail.com,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # Redirect to a thank you page or any other page
        return HttpResponse('Reservation successfully made! Thank you.')

    return render(request, 'reservation.html')


def reviews_view(request):
    # Logic to fetch reviews data from the database or any other source
    reviews = ['Review 1', 'Review 2', 'Review 3']
    return render(request, 'reviews.html', {'reviews': reviews})

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, send email notification to the admin
            send_mail(
                'New Review',
                'A new review has been submitted.',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return redirect('reviews')  # Redirect to the reviews page after submission
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews_list.html', {'reviews': reviews})
    
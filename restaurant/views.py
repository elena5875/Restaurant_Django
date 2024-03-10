#views.py
import logging  

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reservation
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def submit_review(request):
    if request.method == 'POST':
        # Logic to handle review submission
        return HttpResponse('Review submitted successfully!')
    else:
        # Handle GET request (if needed)
        return HttpResponse('Method not allowed.', status=405)

def home(request):
    return render(request, 'home.html')

def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})
    
def reservation_view(request):
    if request.method == 'POST':
        # Handle form submission
        return HttpResponse("Reservation submitted successfully!")
    else:
        # Handle GET request
        # Render the reservation form template with context variables
        context = {
            'hours_range': range(17, 24),
            'people_range': range(1, 10),
        }
        return render(request, 'reservation.html', context)
        
def reviews_view(request):
    # Logic to fetch reviews data from the database or any other source
   
    reviews = ['Review 1', 'Review 2', 'Review 3']
    return render(request, 'reviews.html', {'reviews': reviews})

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

def reservation(request):
    if request.method == 'POST':
        # Retrieve form data
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
        reservation = Reservation.objects.create(date=date, time=time, number_of_people=people, email=email, phone_number=phone)

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
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Replace ADMIN_EMAIL with the actual admin email address
            fail_silently=False,
        )

        # Redirect to a thank you page or any other page
        return HttpResponse('Reservation successfully made! Thank you.')

    return render(request, 'reservation.html')
    
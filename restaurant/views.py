#views.py

import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm
from datetime import datetime
from django.views.generic import FormView

def home(request):
    return render(request, 'home.html')

def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})

def your_reservation_view(request):
    return render(request, 'reservation.html')

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the reservation to the database
            reservation = form.save(commit=False)
            reservation.time = form.cleaned_data['time']  # Use cleaned_data to access validated data
            reservation.save()

            # Mock email notification
            send_mail(
                'Reservation Received',
                'Your reservation has been received successfully.',
                settings.DEFAULT_FROM_EMAIL,
                [reservation.email],
                fail_silently=False,
            )

            # Display success message
            messages.success(request, 'Reservation submitted successfully!')
            return redirect('reservation_view')  # Redirect to the same page to clear the form
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})

class ReservationFormView(FormView):
    template_name = 'reservation_form.html'  # Template for the reservation form
    form_class = ReservationForm  # Your reservation form class
    success_url = '/thank-you/'  # URL to redirect after successful form submission

    def form_valid(self, form):
        # Handle form submission logic here
        # For example, save the form data to the database
        form.save()
        return super().form_valid(form)

def reservation_list_view(request):
    # Retrieve all reservations from the database
    reservations = Reservation.objects.all()
    # Pass the reservations data to the reservation.html template
    return render(request, 'reservation.html', {'reservations': reservations})


def reviews(request):
    # Your view logic here
    pass
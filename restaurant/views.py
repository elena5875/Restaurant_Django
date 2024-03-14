#views.py

import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Reservation, Review
from .forms import ReviewForm, ReservationForm
from .models import Reservation
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})

def your_reservation_view(request):
    return render(request, 'reservation.html')

from .forms import ReservationForm

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

def reviews(request):
    approved_reviews = Review.objects.filter(approved=True)
    return render(request, 'reviews.html', {'reviews': approved_reviews})

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})

def reject_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
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
    return redirect('admin_dashboard')

def review_list(request):
    approved_reviews = Review.objects.filter(approved=True)
    return render(request, 'reviews.html', {'reviews': approved_reviews})

def review_form(request):
    return render(request, 'review_form.html')

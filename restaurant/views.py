## views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Reservation
from .forms import ReservationAdminForm

def home(request):
    return render(request, 'home.html')

def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationAdminForm(request.POST)
        if form.is_valid():
            reservation = form.save()  # Save the form data to the database
            # Send a success email using mock email
            send_mock_email(reservation)
            messages.success(request, 'Reservation submitted successfully!')
            return redirect('reservation_view')
    else:
        form = ReservationAdminForm()

    return render(request, 'reservation.html', {'form': form})

def send_mock_email(reservation):
    # Mock email content
    subject = 'Reservation Received'
    message = f'Your reservation for {reservation.date} at {reservation.time} has been received successfully.'
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_email = reservation.email
    # Send the mock email
    send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)

def approve_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.status = 'confirmed'
    reservation.save()
    send_approval_email(reservation)
    messages.success(request, 'Reservation approved successfully!')
    return redirect('reservation_detail', reservation_id=reservation_id)

def reject_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.status = 'canceled'
    reservation.save()
    send_rejection_email(reservation)
    messages.success(request, 'Reservation rejected successfully!')
    return redirect('reservation_detail', reservation_id=reservation_id)

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    messages.success(request, 'Reservation deleted successfully!')
    return redirect('reservation_list')

    

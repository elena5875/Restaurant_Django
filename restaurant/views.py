## views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Reservation
from .forms import ReservationAdminForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
    return render(request, 'home.html')

def menu_view(request):
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})

def reservation_view(request):
    if request.method == 'POST':
        print("Form submission received")  # Debug statement
        print("POST data:", request.POST)  # Debug statement
        form = ReservationAdminForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug statement
            reservation = form.save()
            send_reservation_confirmation_email(reservation)
            messages.success(request, 'Reservation submitted successfully!')
            return redirect('reservation')
        else:
            print("Form is invalid", form.errors)  # Debug statement
    else:
        form = ReservationAdminForm()
        print("Rendering reservation form")  # Debug statement

    return render(request, 'reservation.html', {'form': form})

def send_reservation_confirmation_email(reservation):
    subject = 'Reservation Received'
    html_message = render_to_string('reservation_success.html', {'reservation': reservation})
    plain_message = strip_tags(html_message)
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_email = reservation.email
    send_mail(subject, plain_message, sender_email, [recipient_email], html_message=html_message)

def approve_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.status = 'confirmed'
    reservation.save()
    send_approval_email(reservation)
    messages.success(request, 'Reservation approved successfully!')
    return redirect('reservation_detail', reservation_id=reservation_id)

def send_approval_email(reservation):
    subject = 'Reservation Approved'
    message = f'Your reservation for {reservation.date} at {reservation.time} has been approved.'
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_email = reservation.email
    send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)

def reject_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.status = 'canceled'
    reservation.save()
    send_rejection_email(reservation)
    messages.success(request, 'Reservation rejected successfully!')
    return redirect('reservation_detail', reservation_id=reservation_id)

def send_rejection_email(reservation):
    subject = 'Reservation Rejected'
    message = f'Your reservation for {reservation.date} at {reservation.time} has been rejected.'
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_email = reservation.email
    send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    messages.success(request, 'Reservation deleted successfully!')
    return redirect('reservation_list')

## views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation, Review, Comment
from .forms import ReservationForm, ReviewForm, CommentForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


def home(request):
    reviews = Review.objects.filter(is_posted=True).order_by('-created_at')
    return render(request, 'home.html', {'reviews': reviews})

def menu_view(request):
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})

def reservation_view(request):
    """
    Handles table reservations.
    Validates the form and creates a reservation if the form is valid.
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            # Prevent reservation for past dates
            if reservation.date < timezone.now().date():
                messages.error(request, 'You cannot make a reservation for a past date.')
                return redirect('reservation')

            # Send confirmation email
            send_reservation_confirmation_email(reservation)
            messages.success(request, 'Reservation submitted successfully and is pending approval!')
            return redirect('reservation_success')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors and try again.')
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})


def send_reservation_confirmation_email(reservation):
    subject = 'Reservation Received'
    html_message = render_to_string('reservation_success.html', {'reservation': reservation})
    plain_message = strip_tags(html_message)
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_email = reservation.email
    send_mail(subject, plain_message, sender_email, [recipient_email], html_message=html_message)

def reservation_success(request):
    return render(request, 'reservation_success.html')

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

def review_list(request):
    reviews = Review.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'review_list.html', {'reviews': reviews})

def review_create(request):
    """
    Handles the review creation.
    Validates the form and creates a review if valid.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_approved = False  # You might want to approve reviews manually
            review.save()
            messages.success(request, 'Review submitted successfully and is pending approval!')
            return redirect('review_list')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors and try again.')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})


def review_detail(request, pk):
    """
    Displays review details and handles comment submission.
    Validates the comment form and saves the comment if valid.
    """
    review = get_object_or_404(Review, pk=pk)
    comments = review.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('review_detail', pk=review.pk)
        else:
            messages.error(request, 'There was an error with your comment. Please correct the errors and try again.')
    else:
        form = CommentForm()

    return render(request, 'review_detail.html', {
        'review': review,
        'comments': comments,
        'form': form
    })

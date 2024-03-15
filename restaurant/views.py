#views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Reservation
from .forms import ReservationAdminForm
from django.views.generic import FormView

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
            reservation = form.save(commit=False)
            reservation.time = form.cleaned_data['time']
            reservation.save()

            send_mail(
                'Reservation Received',
                'Your reservation has been received successfully.',
                settings.DEFAULT_FROM_EMAIL,
                [reservation.email],
                fail_silently=False,
            )

            messages.success(request, 'Reservation submitted successfully!')
            return redirect('reservation_view')
    else:
        form = ReservationAdminForm()

    return render(request, 'reservation.html', {'form': form})

class ReservationFormView(FormView):
    template_name = 'reservation_form.html'
    form_class = ReservationAdminForm
    success_url = '/thank-you/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def reservation_list_view(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html', {'reservations': reservations})

def handle_form_submission(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # If form data is valid, save it to the database
            form.save()
            # Redirect to a success page or any other desired URL
            return redirect('success_page')
    else:
        # If request method is not POST, create a new form instance
        form = ReservationForm()
    
    # Render the template with the form
    return render(request, 'reservation_form.html', {'form': form})
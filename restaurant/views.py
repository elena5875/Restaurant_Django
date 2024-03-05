# restaurant/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .forms import ReviewForm
from .models import Reservation, Review

# Existing views
def home(request):
    return render(request, 'home.html')

def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    # For demonstration purposes 
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})

def reservation_view(request):
    # Logic for reservation view
    return render(request, 'reservation.html')

def reviews_view(request):
    # Logic to fetch reviews data from the database or any other source
    # For demonstration purposes 
    reviews = ['Review 1', 'Review 2', 'Review 3']
    return render(request, 'reviews.html', {'reviews': reviews})

# Combined reservation view and form submission
def reservation(request):
    if request.method == 'POST':
        # Check if it's a reservation form submission
        if 'date' in request.POST:
            date = request.POST.get('date')
            time = request.POST.get('time')
            people = request.POST.get('people')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            # Perform server-side validation
            if not all([date, time, people, email, phone]):
                return HttpResponse('All fields are required.', status=400)

            # Save reservation to the database
            reservation = Reservation.objects.create(date=date, time=time, people=people, email=email, phone=phone)

            # Reservation successful
            return HttpResponse('Reservation successfully made!')
        # Check if it's a review form submission
        elif 'review_text' in request.POST:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                # Additional processing if needed
                review.save()
                return redirect('home')  # Redirect to home page after submission
        else:
            return HttpResponse('Invalid form submission.', status=400)

    return render(request, 'reservation.html')

# View for listing reservations
@login_required
def reservations_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations_list.html', {'reservations': reservations})

# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

# My view function
def my_view(request):
    if request.method == 'POST':
        # Access the POST data
        post_data = request.POST

        # Inspect the POST data
        for key, value in post_data.items():
            print(f"Key: {key}, Value: {value}")

        # Example: Get value of a specific field
        username = post_data.get('username')
        password = post_data.get('password')

        # Example: Perform some action based on the POST data
        if username and password:
            # Process the login credentials
            
            return HttpResponse("Login successful!")
        else:
            # Handle invalid or missing data
            return HttpResponse("Invalid login credentials.")

    # Handle GET request or other HTTP methods
    
    return HttpResponse("This is a GET request.")

def login_view(request):
    if request.method == 'POST':
        # Process the login form submission
        # Handle authentication and other logic here
        pass  # Placeholder for actual login logic
    else:
        # Render the login form
        return render(request, 'login.html')
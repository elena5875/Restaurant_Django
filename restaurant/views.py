#views.py
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

# Your existing views
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

def reservation(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')

        # Perform server-side validation
        if not date or not time or not people:
            return HttpResponse('All fields are required.', status=400)

        # Additional validation logic can be added here
        
        # Reservation successful
        return HttpResponse('Reservation successfully made!')

    return render(request, 'reservation.html')

# New function for handling review submission
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            # Additional processing if needed
            review.save()
            return redirect('home')  # Redirect to home page after submission
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})

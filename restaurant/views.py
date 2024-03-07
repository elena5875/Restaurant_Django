#views.py
from django.shortcuts import render
from django.http import HttpResponse

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
        if not (date and time and people):
            return HttpResponse('All fields are required.', status=400)

        # Additional validation logic can be added here
        
        # Reservation successful
        return HttpResponse('Reservation successfully made!')

    return HttpResponse('Invalid request method.', status=405)

#views.py


from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu_view(request):
    # Logic to fetch menu data from the database or any other source
    # For demonstration purposes, let's assume menu data is stored in a variable named 'menu_items'
    menu_items = ['Item 1', 'Item 2', 'Item 3']
    return render(request, 'menu.html', {'menu_items': menu_items})
    
def reservation_view(request):
    # Logic for reservation view
    return render(request, 'reservation.html')

def reviews_view(request):
    # Logic to fetch reviews data from the database or any other source
    # For demonstration purposes, let's assume reviews data is stored in a variable named 'reviews'
    reviews = ['Review 1', 'Review 2', 'Review 3']
    return render(request, 'reviews.html', {'reviews': reviews})
    
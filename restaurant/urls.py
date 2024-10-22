# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('menu/', views.menu_view, name='menu'),  # Menu page view
    path('reservation/', views.reservation_view, name='reservation'),  # Reservation form view
    path('reservation_success/', views.reservation_success, name='reservation_success'),  # Successful reservation confirmation view
    path('approve/<int:reservation_id>/', views.approve_reservation, name='approve_reservation'),  # Approve a reservation by ID
    path('reject/<int:reservation_id>/', views.reject_reservation, name='reject_reservation'),  # Reject a reservation by ID
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),  # Delete a reservation by ID
    path('reviews/', views.review_list, name='review_list'),  # List of reviews view
    path('reviews/new/', views.review_create, name='review_create'),  # Create a new review view
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),  # Detailed view of a specific review by primary key (pk)
]

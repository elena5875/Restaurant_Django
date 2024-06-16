# urls.py
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('approve/<int:reservation_id>/', views.approve_reservation, name='approve_reservation'),
    path('reject/<int:reservation_id>/', views.reject_reservation, name='reject_reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
]

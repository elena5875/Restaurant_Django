#restaurant/urls.py

from django.contrib import admin
from django.urls import path
from . import views
from .views import reservation_view

urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu_view, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),  
    path('reviews/', views.reviews_view, name='reviews'),
    path('reservation/', reservation_view, name='reservation_view'),
    path('submit_review/', views.submit_review, name='submit_review')

]

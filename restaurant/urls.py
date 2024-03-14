#urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu_view, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),
    path('reviews/', views.review_list, name='reviews'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('review_form/', views.review_form, name='review_form'),
    path('reservation/', views.reservation_view, name='reservation_view'),
]

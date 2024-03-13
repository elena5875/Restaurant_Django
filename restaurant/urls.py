#restaurant/urls.py
from django.urls import path
from . import views
from .views import reservation_view
from .views import review_form, reviews_list


urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu_view, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),
    path('reservation/', reservation_view, name='reservation_view'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('review_form/', review_form, name='review_form'),
    path('reviews_list/', reviews_list, name='reviews_list'), 
]

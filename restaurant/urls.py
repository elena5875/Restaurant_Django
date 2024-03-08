#restaurant/urls.py
from django.urls import path
from . import views  

app_name = 'restaurant' 

urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu_view, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),  
    path('reviews/', views.reviews_view, name='reviews'),
]

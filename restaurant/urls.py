#urls.py

from django.urls import path
from . import views
from .views import ReservationFormView

urlpatterns = [
    path('', views.home, name='home'), 
    path('menu/', views.menu_view, name='menu'),
    path('reservation/', views.reservation_view, name='reservation'),
    path('reservation_form/', ReservationFormView.as_view(), name='reservation_form'), 
    path('reservations/', views.reservation_list_view, name='reservation_list'), 
]

"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#urls.py


# Import necessary modules
from django.contrib import admin
from django.urls import path
from restaurant.views import home, menu_view, reservation_view, reviews_view

# Define the contact view function
def contact_view(request):
    return HttpResponse("This is the contact page")  # Example response, replace with your own logic

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('menu/', menu_view, name='menu'),
    path('reservation/', reservation_view, name='reservation'),  
    path('reviews/', reviews_view, name='reviews'),
    path('contact/', contact_view, name='contact'),  # Define a URL pattern for the contact page
]

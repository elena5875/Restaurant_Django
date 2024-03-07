#admin.py

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.shortcuts import redirect

# Apply the staff_member_required decorator to the admin login view
admin.site.login = staff_member_required(admin.site.login)

# Register your models here
from .models import Reservation

admin.site.register(Reservation)

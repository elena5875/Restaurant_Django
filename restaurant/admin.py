from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.admin.widgets import AdminTimeWidget
from django import forms
from .models import Reservation

class ReservationAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.Select(choices=self.get_time_choices())

    def get_time_choices(self):
        time_slots = []
        start_time = 17  # 5:00 PM in 24-hour format
        end_time = 23    # 11:00 PM in 24-hour format
        for hour in range(start_time, end_time + 1):
            for minute in ['00', '30']:
                time = f"{hour}:{minute}"
                time_slots.append((time, f"{hour}:{minute}"))  # Appending tuple of (value, label)
        return time_slots

    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationAdminForm
    list_display = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people', 'status']
    list_filter = ['date', 'time', 'status']
    search_fields = ['name', 'email', 'phone_number']
    actions = ['approve_reservations', 'reject_reservations', 'delete_reservations']

    def approve_reservations(self, request, queryset):
        queryset.update(status='confirmed')
        self.send_approval_email(queryset)

    def reject_reservations(self, request, queryset):
        queryset.update(status='canceled')
        self.send_rejection_email(queryset)

    def delete_reservations(self, request, queryset):
        queryset.delete()

    def send_rejection_email(self, reservations):
        subject = 'Reservation Rejected'
        for reservation in reservations:
            message = render_to_string('reservation_rejected_email.html', {'reservation': reservation})
            plain_message = strip_tags(message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [reservation.email], html_message=message)
    
    def send_approval_email(self, reservations):
        subject = 'Reservation Approved'
        for reservation in reservations:
            message = render_to_string('reservation_approved_email.html', {'reservation': reservation})
            plain_message = strip_tags(message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [reservation.email], html_message=message)

admin.site.register(Reservation, ReservationAdmin)




#admin.py

from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Reservation, Review, Comment
from .forms import ReservationAdminForm

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


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['name', 'email']
    inlines = [CommentInline]
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
    approve_reviews.short_description = "Approve selected reviews"

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)

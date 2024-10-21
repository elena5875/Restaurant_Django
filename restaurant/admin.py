#admin.py

from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .forms import ReservationAdminForm  
from .models import Reservation, Review, Comment 
from django.contrib import messages
from django.contrib import admin, messages


class ReservationAdmin(admin.ModelAdmin):
    form = ReservationAdminForm
    list_display = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people', 'status']
    list_filter = ['date', 'time', 'status']
    search_fields = ['name', 'email', 'phone_number']
    actions = ['approve_reservations', 'reject_reservations', ]

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
    list_display = ['name', 'email', 'is_approved', 'is_posted', 'created_at']
    list_filter = ['is_approved', 'is_posted', 'created_at']
    search_fields = ['name', 'email']
    inlines = [CommentInline]
    actions = ['approve_reviews', 'reject_reviews', 'post_reviews']  # Remove 'delete_reviews'

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
        self.send_email(queryset, 'approved')
        messages.success(request, "Selected reviews were approved successfully.")

    def reject_reviews(self, request, queryset):
        queryset.update(is_approved=False)
        self.send_email(queryset, 'rejected')
        messages.warning(request, "Selected reviews were rejected successfully.")

    def post_reviews(self, request, queryset):
        queryset.update(is_posted=True)
        self.send_email(queryset, 'posted')
        messages.success(request, "Selected reviews were posted successfully.")

    def delete_reviews(self, request, queryset):
        queryset.delete()
        messages.warning(request, "Selected reviews were deleted successfully.")  # Use messages.warning for warnings

    def send_email(self, queryset, status):
        subject = f'Review {status.capitalize()}'
        for review in queryset:
            if status == 'approved':
                message = render_to_string('review_approved.html', {'review': review})
            elif status == 'rejected':
                message = render_to_string('review_rejected.html', {'review': review})
            else:
                message = render_to_string('review_posted.html', {'review': review})
            plain_message = strip_tags(message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [review.email], html_message=message)

    approve_reviews.short_description = "Approve selected reviews"
    reject_reviews.short_description = "Reject selected reviews"
    post_reviews.short_description = "Post selected reviews"
    delete_reviews.short_description = "Delete selected reviews"

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
admin.site.register(Reservation, ReservationAdmin)

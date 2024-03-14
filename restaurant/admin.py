from django.contrib import admin
from django.core.mail import send_mail
from .models import Reservation, Review
from .utils import reject_review

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people', 'status']
    list_filter = ['date', 'time', 'status']
    search_fields = ['name', 'email', 'phone_number']
    actions = ['approve_reservations', 'reject_reservations', 'cancel_reservation']

    def approve_reservations(self, request, queryset):
        queryset.update(approved=True)

    def reject_reservations(self, request, queryset):
        queryset.update(approved=False)

    def cancel_reservation(self, request, queryset):
        for reservation in queryset:
            # Update reservation status to canceled
            reservation.status = 'canceled'
            reservation.save()

    approve_reservations.short_description = "Approve selected reservations"
    reject_reservations.short_description = "Reject selected reservations"
    cancel_reservation.short_description = "Cancel selected reservations"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'approved', 'created_at']
    actions = [reject_review]

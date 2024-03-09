# admin.py
from django.contrib import admin
from django.core.mail import send_mail
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people', 'status']
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ['date', 'time', 'status']
    
    NUMBER_OF_PEOPLE_CHOICES = [(str(i), str(i)) for i in range(1, 10)]
    
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'number_of_people':
            kwargs['choices'] = self.NUMBER_OF_PEOPLE_CHOICES
        return super().formfield_for_choice_field(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['time'].widget.attrs['min'] = '17:00'
        form.base_fields['time'].widget.attrs['max'] = '23:00'
        return form

    # Define actions
    def confirm_reservation(self, request, queryset):
        for reservation in queryset:
            # Update reservation status to confirmed
            reservation.status = 'confirmed'
            reservation.save()

            # Send confirmation email
            send_mail(
                'Reservation Confirmed',
                'Your reservation has been confirmed.',
                'from@example.com',
                [reservation.email],
                fail_silently=False,
            )
    confirm_reservation.short_description = "Confirm selected reservations"
    
    def cancel_reservation(self, request, queryset):
        for reservation in queryset:
            # Update reservation status to canceled
            reservation.status = 'canceled'
            reservation.save()

            # Send cancellation email
            send_mail(
                'Reservation Canceled',
                'Your reservation has been canceled.',
                'from@example.com',
                [reservation.email],
                fail_silently=False,
            )
    cancel_reservation.short_description = "Cancel selected reservations"

    actions = [confirm_reservation, cancel_reservation]

admin.site.register(Reservation, ReservationAdmin)

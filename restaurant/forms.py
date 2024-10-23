from django import forms
from .models import Reservation, Review, Comment
import datetime

# ReservationAdminForm for managing reservations in the admin panel
class ReservationAdminForm(forms.ModelForm):
    """
    Form for managing reservations in the Django admin panel.

    This form provides a customized interface for admin users to create
    and manage reservations, including time and number of people.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set time choices as dropdown options
        self.fields['time'].widget = forms.Select(choices=self.get_time_choices())
        # Set the number of people choices from 1 to 9
        self.fields['number_of_people'].widget = forms.Select(choices=[(i, i) for i in range(1, 10)])

    def get_time_choices(self):
        """
        Define time slots for admin reservation management.

        Returns:
            list: A list of tuples representing time choices for reservations.
        """
        time_slots = []
        start_time = 15  # 3:00 PM in 24-hour format
        end_time = 23    # 11:00 PM in 24-hour format
        for hour in range(start_time, end_time + 1):
            for minute in ['00', '30']:
                time = f"{hour}:{minute}"
                time_slots.append((time, f"{hour}:{minute}"))  # Appending tuple of (value, label)
        return time_slots

    class Meta:
        model = Reservation
        fields = '__all__'

    def clean_number_of_people(self):
        """
        Validate the number of people for the reservation.

        Returns:
            int: The validated number of people.

        Raises:
            forms.ValidationError: If the number of people exceeds 9.
        """
        number_of_people = self.cleaned_data['number_of_people']
        if number_of_people > 9:
            raise forms.ValidationError("You can reserve a maximum of 9 people. For larger groups, please call the restaurant.")
        return number_of_people

    def clean_time(self):
        """
        Validate the selected reservation time.

        Returns:
            datetime.time: The validated time.

        Raises:
            forms.ValidationError: If the selected time is outside the allowed range.
        """
        time_str = self.cleaned_data['time']
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        min_time = datetime.time(15, 0)  # 3 PM
        max_time = datetime.time(23, 0)  # 11 PM
        if time < min_time or time > max_time:
            raise forms.ValidationError("Please select a time between 3 PM and 11 PM.")
        return time

    def clean_date(self):
        """
        Validate the reservation date.

        Returns:
            datetime.date: The validated reservation date.

        Raises:
            forms.ValidationError: If the reservation date is in the past.
        """
        reservation_date = self.cleaned_data['date']
        if reservation_date < datetime.date.today():
            raise forms.ValidationError("Reservation date cannot be in the past.")
        return reservation_date


from django import forms
from .models import Reservation
import datetime

class ReservationForm(forms.ModelForm):
    """
    Form for customers to make reservations on the website.
    """
    
    # Placeholder for date field
    date = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Select Year", "Select Month", "Select Day")))

    # Define time choices: From 3 PM to 11 PM with 30-minute intervals
    TIME_CHOICES = [
        ('', 'Select a time'),  # Placeholder option
    ] + [
        (datetime.time(hour, minute).strftime('%H:%M'), datetime.time(hour, minute).strftime('%I:%M %p'))
        for hour in range(15, 24) for minute in (0, 30)
    ]

    time = forms.ChoiceField(choices=TIME_CHOICES, required=True)

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the number of people choices from 1 to 9, with a placeholder option
        self.fields['number_of_people'].widget = forms.Select(choices=[('', 'Select number of people')] + [(i, i) for i in range(1, 10)])

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data['number_of_people']
        if number_of_people > 9:
            raise forms.ValidationError("You can reserve a maximum of 9 people. For larger groups, please call the restaurant.")
        return number_of_people

    def clean_time(self):
        time_str = self.cleaned_data['time']
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        min_time = datetime.time(15, 0)  # 3 PM
        max_time = datetime.time(23, 0)  # 11 PM
        if time < min_time or time > max_time:
            raise forms.ValidationError("Please select a time between 3 PM and 11 PM.")
        return time

    def clean_date(self):
        reservation_date = self.cleaned_data['date']
        if reservation_date < datetime.date.today():
            raise forms.ValidationError("Reservation date cannot be in the past.")
        return reservation_date



class ReviewForm(forms.ModelForm):
    """
    Form for submitting reviews by customers.

    This form provides an interface for customers to input their review details,
    including name, email, and review text.
    """
    
    class Meta:
        model = Review
        fields = ['name', 'email', 'review_text']


class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on reviews.

    This form provides an interface for users to input their comment text.
    """
    
    class Meta:
        model = Comment
        fields = ['comment_text']

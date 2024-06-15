#forms.py
from django import forms
from .models import Reservation
import datetime

class ReservationAdminForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    # Define the time choices for the dropdown
    TIME_CHOICES = [
        (datetime.time(hour, minute).strftime('%H:%M'), datetime.time(hour, minute).strftime('%I:%M %p'))
        for hour in range(15, 24) for minute in (0, 30)
    ]
    time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone_number', 'date', 'time', 'number_of_people']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number_of_people'].widget = forms.Select(choices=[(i, i) for i in range(1, 10)])

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data['number_of_people']
        if number_of_people > 9:
            raise forms.ValidationError("You can reserve a maximum of 9 people. For larger groups, please call the restaurant at 012365498.")
        return number_of_people

    def clean_time(self):
        time_str = self.cleaned_data['time']
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        min_time = datetime.time(15, 0)  # 3 PM
        max_time = datetime.time(23, 0)  # 11 PM
        if time < min_time or time > max_time:
            raise forms.ValidationError("Please select a time between 3 PM and 11 PM.")
        return time

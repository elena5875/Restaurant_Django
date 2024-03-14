#forms.py

from django import forms
from .models import Reservation
from .models import Review


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['time', 'number_of_people']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number_of_people'].widget = forms.Select(choices=[(i, i) for i in range(1, 10)])
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']
        

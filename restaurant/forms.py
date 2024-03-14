#forms.py

from django.contrib.admin.widgets import AdminTimeWidget
from django import forms
from .models import Reservation

class CustomAdminTimeWidget(AdminTimeWidget):
    def __init__(self, attrs=None, format=None):
        default_attrs = {'step': '3600'}  # Set step to 1 hour (3600 seconds)
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs, format=format)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['is_hidden'] = self.is_hidden
        context['widget']['required'] = self.is_required
        context['widget']['value'] = self.format_value(value)

        # Limit time range to 5 PM to 11 PM
        context['widget']['attrs']['min'] = '17:00'  # 5 PM
        context['widget']['attrs']['max'] = '23:00'  # 11 PM

        return context

class ReservationAdminForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=CustomAdminTimeWidget())

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

class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=CustomAdminTimeWidget())

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
class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    
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
        

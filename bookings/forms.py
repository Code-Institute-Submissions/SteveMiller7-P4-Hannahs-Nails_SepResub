from datetime import date

from django import forms
from datetimewidget.widgets import DateTimeWidget

from .models import Appointments


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointments
        fields = ('nail_tech', 'date', 'timeslot', 'phone_number')
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
                ),
        }

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
        if day.isoweekday() in (1, 7):
            raise forms.ValidationError("Sorry! We are closed on a Sunday and a Monday", code='invalid')

        return day

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
        # widgets = {
        #     'date': DateTimeWidget(
        #         attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
        #         options={
        #             'minView': 2,  # month view
        #             'maxView': 3,  # year view
        #             'weekStart': 1,
        #             'todayHighlight': True,
        #             'format': 'yyyy-mm-dd',
        #             'daysOfWeekDisabled': [0, 1],
        #             'startDate': date.today().strftime('%Y-%m-%d'),
        #         }),
        # }

    def clean_date(self):
        day = self.cleaned_data['date']

        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming (tomorrow or later)', code='invalid')
        if day.isoweekday() in (0, 1):
            raise forms.ValidationError("Sorry! We are closed on a Sunday and a Monday", code='invalid')

        return day
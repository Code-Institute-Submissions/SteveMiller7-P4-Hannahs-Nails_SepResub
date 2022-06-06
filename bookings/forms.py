from datetime import date

from django import forms
from datetimewidget.widgets import DateTimeWidget

from .models import Schedule




class SchedulePage(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('date', 'slot',)
        
        # widgets = {
        #         'date': DateTimeWidget(
        #             attrs={'id': "date"}, usel10n = True, bootstrap_version=3,
        #             options={
        #                 'weekStart': 1,
        #                 'todayHighlight': True,
        #                 'format': 'yyyy-mm-dd',
        #                 'daysOfTheWeekDisabled': [0, 1],
        #                 'startDate': date.today().strftime('%Y-%m-%d'),
        #             }
        #         ),
        # }

    # Below function stops bookings being made on the day and at weekends

    # def clean_date(self):
    #     day = self.Cleaned_data['date']

    #     if day <= date.today():
    #         raise forms.ValidationError('Uh oh! Online bookings cannot be made on the day. Please contact us direct on 01764 660068. Thank you')
    #     if day.isweekday() in (0, 6):
    #         raise forms.ValidationError ('Oops! We are closed on Sundays and Mondays. Please choose an alternative day. Thank you')

    #         return day

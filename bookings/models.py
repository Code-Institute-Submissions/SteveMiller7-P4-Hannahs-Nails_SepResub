from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


class Photo(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    

class Appointments(models.Model):
    """Contains info about appointment"""

    class Meta:
        unique_together = ('nail_tech', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '9am - 9.45am'),
        (1, '9.45am - 10.30am'),
        (2, '10.30am - 11.15am'),
        (3, '11.15am - 12pm'),
        (4, '12.30pm - 1.15pm'),
        (5, '1.15pm - 2pm'),
        (6, '2pm - 2.45pm'), 
        (7, '2.45pm - 3.30pm'),
        (8, '3.30pm - 4.15pm'),
        (7, '4.15pm - 5pm'),
    )

    nail_tech = models.ForeignKey('Technician',on_delete = models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    phone_number = models.CharField(max_length=20, blank=True, null=True, help_text="Required")
    user = models.ForeignKey(User, default='', null=True, on_delete=models.CASCADE,)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.timeslot, self.nail_tech, self.user, self.phone_number,)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]


class Technician(models.Model):
    """Stores info about doctor"""

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.short_name)

    @property
    def short_name(self):
        return '{} {}.'.format(self.last_name.title(), self.first_name[0].upper())
   
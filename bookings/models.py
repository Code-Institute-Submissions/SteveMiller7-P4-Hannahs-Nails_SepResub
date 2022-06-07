from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


# class Technician(models.Model):
#     title = models.CharField(max_length=40)
#     featured_image = CloudinaryField('image', default='placeholder')
#     background_info = models.TextField(max_length=250)

#     def __str__(self):
#         return self.title


# class Customer(models.Model):
#     name = models.CharField(max_length=40, unique=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=11, unique=True)
#     # address_1 = models.CharField(_("Address line 1"), max_length=100)
#     # address_2 = models.CharField(_("Address line 2"), max_length=100)
#     # city = models.CharField(_("City/Town"), max_length=30)
#     # post_code = models.CharField(_("Postcode"), max_length=10)

#     def __str__(self):
#         return self.name


class Photo(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    
# class Schedule(models.Model):

#     unique_together = ('date_of', 'slot', 'owner')

#     Slots_List = (
#         (0, '9am - 9.45am'),
#         (1, '9.45am - 10.30am'),
#         (2, '10.30am - 11.15am'),
#         (3, '11.15am - 12pm'),
#         (4, '12.30pm - 1.15pm'),
#         (5, '1.15pm - 2pm'),
#         (6, '2pm - 2.45pm'),
#         (7, '2.45pm - 3.30pm'),
#         (8, '3.30pm - 4.15pm'),
#         (7, '4.15pm - 5pm'),
#     )
    
#     date_of = models.DateField(help_text="YYYY-MM-DD")
#     slot = models.IntegerField(choices=Slots_List)
#     owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)



# New code
class Appointments(models.Model):
    """Contains info about appointment"""

    class Meta:
        unique_together = ('nail_tech', 'date', 'timeslot',)

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
    customer_name = models.CharField(max_length=60)
    # phone_number = models.CharField(max_length=20, blank=True, null=True, help_text="Required")

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.timeslot, self.nail_tech, self.customer_name)

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
   

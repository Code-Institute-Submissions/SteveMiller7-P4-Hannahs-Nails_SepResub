from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Technician(models.Model):
    title = models.CharField(max_length=40)
    featured_image = CloudinaryField('image', default='placeholder')
    background_info = models.TextField(max_length=250)

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    # address_1 = models.CharField(_("Address line 1"), max_length=100)
    # address_2 = models.CharField(_("Address line 2"), max_length=100)
    # city = models.CharField(_("City/Town"), max_length=30)
    # post_code = models.CharField(_("Postcode"), max_length=10)

    def __str__(self):
        return self.name


class Photo(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    
class Scheduler(models.Model):

    unique_together = ('customer', 'date', 'slot')

    Slots_List = (
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

    date = models.DateField(help_text="yyyy-mm-dd")
    slot = models.IntegerField(choices=Slots_List)
    customer = models.ForeignKey('Customer', on_delete = models.CASCADE)



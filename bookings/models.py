from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Technician(models.Model):
    title = models.CharField(max_length=40, unique=True)
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
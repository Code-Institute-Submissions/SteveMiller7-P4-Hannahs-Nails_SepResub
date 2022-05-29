from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Technician(models.Model):
    title = models.CharField(max_length=40, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    background_info = models.TextField(max_length=250)

    def __str__(self):
        return self.title

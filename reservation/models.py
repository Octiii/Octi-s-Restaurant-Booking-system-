from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='Your email here.')
    phone = models.BigIntegerField(default='0', blank=True)
    persons = models.BigIntegerField(default='0', blank=True) 
    date = models.DateTimeField(default=datetime.now, blank=True) 

    def __str__(self):
        return self.name
        

class dish(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=5000)
    featured_image = CloudinaryField("image", default='palceholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
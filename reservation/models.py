from django.db import models
from datetime import datetime

# Create your models here.


class reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default='Your email here.')
    phone = models.IntegerField(default='0', blank=True)
    persons = models.IntegerField(default='0', blank=True) 
    date = models.DateTimeField(default=datetime.now, blank=True) 

    def __str__(self):
        return self.name
        
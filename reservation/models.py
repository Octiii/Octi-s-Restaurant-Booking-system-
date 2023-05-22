from django.db import models
from datetime import datetime

# Create your models here.


class reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default='Your email here.')
    phone = models.IntegerField(max_length=12, default='0', blank=True)
    persons = models.IntegerField(max_length=2, default='0', blank=True) 
    date = models.DateTimeField(default=datetime.now, blank=True) 

    def __str__(self):
        return self.name
        
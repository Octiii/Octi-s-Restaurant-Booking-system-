from django.db import models

# Create your models here.


class reservation(models.Model):
    name = models.CharField(max_length=50)
#    email = models.EmailField()
#    phone = models.IntegerField()
#    persons = models.IntegerField() 
#    date = models.DateField() 
#    time = models.TimeField()

    def __str__(self):
        return self.name
        
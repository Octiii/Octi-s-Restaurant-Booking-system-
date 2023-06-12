from django.contrib import admin
from .models import reservation, dish

# Register your models here.

admin.site.register(reservation)
admin.site.register(dish)
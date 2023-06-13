from django.contrib import admin
from .models import reservation, dish
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class dishAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(reservation)
admin.site.register(dish, dishAdmin)


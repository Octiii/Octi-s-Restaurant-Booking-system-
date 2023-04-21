from django.shortcuts import render
from django.views import generic
from .models import reservation


# Create your views here.

from reservation.models import reservation 


def reserv_table(request):
    reservations = reservation.objects.all()
    context = {
        'reservations' : reservations
    }
    if request.method == 'POST':
        name = request.POST.get('reservation_name')
        reservation.objects.create(name=name)

    return render(request ,'reservation/reservation.html' , context)

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import reservation
import datetime

def home(self):
    return render(self, 'reservation/home.html')

def reserv_table(request):
    person = reservation.objects.all()
    context = {
        'person' : person
    }
    if request.method == 'POST':
        name = request.POST.get('reservation_name')
        email = request.POST.get('email_name')
        phone = request.POST.get('number_name')
        persons = request.POST.get('number_persons')
        date = request.POST.get('date_time')
        reservation.objects.create(name=name, email=email, phone=phone, persons=persons, date=date)
    return render(request, 'reservation/reservation.html', context)


def bookings_navigation(self):
    person = reservation.objects.all()
    context = {
        'person' : person
    }
    return render(self, 'reservation/bookings.html', context)


def delete_reservation(request, reserv_id):
    reserv = get_object_or_404(reservation, id=reserv_id)
    reserv.delete()

    return redirect('bookings_navigation')
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import reservation


def reserv_table(request):
    reservations = reservation.objects.all()
    context = {
        'reservations' : reservations
    }
    if request.method == 'POST':
        name = request.POST.get('reservation_name')
        reservation.objects.create(name=name)

    return render(request, 'reservation/reservation.html', context)


def delete_reservation(request, reservations_id):
    reserv = get_object_or_404(reservation, id=reservations_id)
    reserv.delete()

    return redirect('/')

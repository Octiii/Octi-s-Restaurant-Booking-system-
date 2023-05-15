from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import reservation


def reserv_table(request):
    person = reservation.objects.all()
    context = {
        'person' : person
    }
    if request.method == 'POST':
        name = request.POST.get('reservation_name')
        email = request.POST.get('email_name')
        reservation.objects.create(name=name, email=email)
    return render(request, 'reservation/reservation.html', context)


def delete_reservation(request, reserv_id):
    reserv = get_object_or_404(reservation, id=reserv_id)
    reserv.delete()

    return redirect('/')

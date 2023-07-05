from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import reservation, dish
from .forms import dishForm
import datetime



def home(self):
    return render(self, 'home.html')


#def menu(self):
 #   menuItem = dish.objects.all()
 #   context = {
 #       'menuItem' : menuItem
 #   }
 #   return render(self, 'reservation/menu.html',context)


 #Bookings Code


def bookings_navigation(self):
    person = reservation.objects.all()
    context = {
        'person' : person
    }
    return render(self, 'bookings.html', context)


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
    return render(request, 'reservation.html', context)


def delete_reservation(request, reserv_id):
    reserv = get_object_or_404(reservation, id=reserv_id)
    reserv.delete()

    return redirect('bookings_navigation')


#Dish Code


class dishList(generic.ListView):
    model = dish
    queryset = dish.objects.all()
    template_name = 'menu.html'


class MakeDish(generic.CreateView):
    model = dish
    form_class = dishForm
    template_name = 'dishmaker.html'
    success_url = 'menu'
    success_mesage = 'New dish added!'

    def get_context_data(self, **kwargs):
        context = super(MakeDish, self).get_context_data(**kwargs)
        context['photos'] = dish.objects.all().order_by('-created_on')
        return context


#def make_dish(request):
#    menuItem = dish.objects.all()
#    context = {
#        'menuItem' : menuItem
#    }
#    if request.method == 'POST':
#        name = request.POST.get('dish_name')
#        text = request.POST.get('dish_text')
#        dish.objects.create(name=name, text=text)
#    return render(request, 'menu.html', dishList)






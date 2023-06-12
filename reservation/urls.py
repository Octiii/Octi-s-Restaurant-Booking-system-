from reservation import views
from django.urls import path
from django.contrib import admin




urlpatterns = [
    path('', views.home, name='home'),# The '' - need to match -> HTML. After , is the view name you want to link it to. Name parameter has no function as of now. 
    path('home', views.home, name='home'),
    path('menu', views.dishList.as_view(), name='menu'),
    path('make_dish', views.make_dish, name='make_dish'),
    path('reserv_table', views.reserv_table, name='reserv_table'),
    path('bookings_navigation', views.bookings_navigation, name='bookings_navigation'),
    path('delete/<reserv_id>', views.delete_reservation, name='delete'),
]

# Gotcha, okay so the home template will need to be rendered in one of the views. Conventionally, you can call this home if you want. So you would have:
#def home():
#    return render(request, reservation/home.html)
#Then, in your urls.py you would have:
#path('', views.home, name='home'),
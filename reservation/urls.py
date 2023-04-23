from reservation import views
from django.urls import path
from django.contrib import admin




urlpatterns = [
    path('', views.reserv_table, name='reserv_table'),# The '' bit need to have the same name as the lin in the HTML. After , is the view name you want to link it to. Name parameter has no function as of now. 
    path('reserv_table', views.reserv_table, name='reserv_table'),
    path('delete/<reservations_id>', views.delete_reservation, name='delete'),
]

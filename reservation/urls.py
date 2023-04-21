from . import views
from django.urls import path
from django.contrib import admin




urlpatterns = [
    path('reserv_table', views.reserv_table, name='reserv_table'),
]

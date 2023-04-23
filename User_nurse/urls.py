from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Nurses,name='Nurses'),
    path('apply/<int:id>/',views.Apply,name='Apply'),
    path('Work_applied/',views.Work_applied,name='Work_applied')
]

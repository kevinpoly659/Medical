from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Mediator_login,name="Mediator_login"),
    path('Mediators/',views.Mediators,name="Mediators"),
    path('Hospital_users/',views.Hospital_users,name="Hospital_users"),
    path('Nurse_users/',views.Nurse_users,name="Nurse_users"),
    path('Posted_jobs/<int:id>/',views.Posted_jobs,name="Posted_jobs"),
    path('Applied_jobs/<int:id>/',views.Applied_jobs,name="Applied_jobs"),
    path('Create_hospital/',views.Create_hospital,name="Create_hospital"),
    path('Create_nurse/',views.Create_nurse,name="Create_nurse"),
    path('Create_mediator/',views.Create_mediator,name="Create_mediator"),

]

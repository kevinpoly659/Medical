from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Hospitals,name='Hospitals'),
    path('create_job/',views.create_job,name='create_job'),
    path('Applications/<int:id>/',views.Applications,name='Applications'),
    path('Accept/<int:id>',views.Accept,name="Accept"),
    path('Reject/<int:id>',views.Reject,name="Reject"),
    path('Delete_job/<int:id>',views.Delete_job,name="Delete_job"),

]

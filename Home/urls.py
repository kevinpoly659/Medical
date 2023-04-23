from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('hospital_login/',views.hospital_login,name="hospital_login"),
    path('nurse_login/',views.nurse_login,name="nurse_login"),
    path('account_application/',views.Account_application,name="Account_application"),
    path('Logout',views.Logout,name='Logout'),
]
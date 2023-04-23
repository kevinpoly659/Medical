from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Accounts.models import Hospital,Nurse,Account_requests
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'index.html')


def hospital_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        try:
            login(request,user)
            Hospital.objects.get(user=user)
            return redirect('Hospitals')
        except:
            messages.error(request,"You'r not authorized to access this page")



    return render(request,'login.html')

def nurse_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        try:
            login(request,user)
            Nurse.objects.get(user=user)
            return redirect('Nurses')
        except:
            messages.error(request,"You'r not authorized to access this page")



    return render(request,'nurse/nurse_login.html')


def Account_application(request):
    if request.method == 'POST':
    
        full_name=request.POST['full_name']
        if len(full_name)<1:
            messages.info(request,"Full Name field empty")
            return redirect('Account_application')
        
        email=request.POST['email']
        if len(email)<1:
            messages.info(request,"Email field empty")
            return redirect('Account_application')

        type=request.POST['type']
        acc = Account_requests.objects.create(full_name=full_name,email=email,account_type=type)
        acc.save()
        return redirect('home')


    return render(request,'account_application.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('home')
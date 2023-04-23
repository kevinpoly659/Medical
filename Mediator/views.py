from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Accounts.models import *
from django.contrib.auth.models import Group
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Mediators(request):
    users=Mediator.objects.all()

    
    return render(request,'mediator/mediator.html',{'users':users})



def Mediator_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('Mediators')
        else:
            messages.error(request,"!!!!!!!!")

    return render(request,'mediator/mediator_login.html')

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Hospital_users(request):
    users = Hospital.objects.all()

    return render(request,'mediator/hospitals_users.html',{'users':users})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Nurse_users(request):
    users = Nurse.objects.all()

    return render(request,'mediator/nurses_users.html',{'users':users})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Posted_jobs(request,id):
    try:
        hospital = Hospital.objects.get(id=id)
        job = WorkShift.objects.filter(hospital=hospital)
    except:
        print("safafcas")
        job = []
    
    return render(request,'mediator/jobs.html',{'jobs':job})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Applied_jobs(request,id):
    try:
        nurse = Nurse.objects.get(id=id)
        job=ShiftApplication.objects.filter(nurse=nurse)
    except:
        job=[]

    return render(request,'mediator/applied_jobs.html',{'jobs':job})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Create_hospital(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if username is None:
                messages.info(request,"Username Should not be empty")
                return redirect('Create_hospital')
            if len(password1) < 6:
                messages.info(request,"Password length should be at least 6")
                return redirect('Create_hospital')
            if email is None:
                messages.info(request,"Incorrect Email")
            if password1 == password2:
                user1 = User.objects.create_user(username=username,password=password1,email=email)
                mediator = Mediator.objects.get(user=request.user)
                hospital=Hospital.objects.create(user=user1,mediator=mediator)
                user1.save()
                user1 = User.objects.get(username=username)
                user1.groups.add(1)
                user1.save()
                hospital.save()            
                return redirect('Hospital_users')
            else:
                messages.info(request,"Password Mismatch")
    except:
        messages.info(request,"Something went wrong please try again")    



    return render(request,'mediator/create_hospital.html')
    

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Create_nurse(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if username is None:
                messages.info(request,"Username Should not be empty")
                return redirect('Create_hospital')
            if len(password1) < 6:
                messages.info(request,"Password length should be at least 6")
                return redirect('Create_hospital')
            if email is None:
                messages.info(request,"Incorrect Email")
            if password1 == password2:
                user1 = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                mediator = Mediator.objects.get(user=request.user)
                nurse=Nurse.objects.create(user=user1,mediator=mediator)
                user1.save()
                user1 = User.objects.get(username=username)
                user1.groups.add(2)
                user1.save()
                nurse.save()            
                return redirect('Nurse_users')
            else:
                messages.info(request,"Password Mismatch")
    except:
        messages.info(request,"Something went wrong please try again")    



    return render(request,'mediator/create_nurse.html')



def Create_mediator(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if len(username) is None:
                messages.info(request,"Username Should not be empty")
                return redirect('Create_mediator')
            if len(password1) < 6:
                messages.info(request,"Password length should be at least 6")
                return redirect('Create_mediator')
            if len(email) is None:
                messages.info(request,"Incorrect Email")
                return redirect('Create_mediator')
            if password1 == password2:
                try:
                    user1 = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user1.save()
                    user1=User.objects.get(username=username)     
                    user1.is_staff = True
                    user1.is_superuser = True   
                    mediator = Mediator.objects.create(user=user1)  
                    user1.groups.add(3)
                    user1.save()
                    mediator.save()
                    return redirect('Mediators')
                except:
                    messages.info(request,"Incorrect Email")
                    return redirect('Create_mediator')
            else:
                messages.info(request,"Password Mismatch")
                return redirect('Create_mediator')

    except:
        messages.info(request,"Something went wrong please try again")    



    return render(request,'mediator/create_mediator.html')
        
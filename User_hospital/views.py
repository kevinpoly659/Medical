from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Accounts.models import WorkShift,Hospital,ShiftApplication
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Hospitals(request):
    try:
        obj = WorkShift.objects.filter(hospital = Hospital.objects.get(user=request.user))
    except:
        return redirect('Hospitals')

    return render(request,'hospital/hospital.html',{'jobs':obj})

@login_required
def Applications(request,id):
    
    shift = WorkShift.objects.get(id=id)
    obj = ShiftApplication.objects.all()
    l=[]
    for i in obj:
        if i.shift == shift:
            l.append(i)

    
    return render(request,'hospital/applications.html',{'jobs':l})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_job(request):

    if request.method == 'POST':
        title=request.POST['title']
        if len(title)<1:
            messages.info(request,"Title field is empty")
            return redirect('create_job')
        location=request.POST['location']
        if len(location)<1:
            messages.info(request,"Location Field is empty")
            return redirect('create_job')

        time=request.POST['time']
        if time is None:
            messages.info(request,"Location Field is empty")
            return redirect('create_job')

        date=request.POST['date']
        if date is None:
            messages.info(request,"Location Field is empty")
            return redirect('create_job')

        price_per_hour=request.POST['price_per_hour']
        if str(price_per_hour).isdecimal():
            messages.info(request,"Price Field is empty")
            return redirect('create_job')

        hospital = Hospital.objects.get(user=request.user)

        obj = WorkShift.objects.create(title=title,
                                      hospital=hospital,
                                      location=location,
                                      time=time,
                                      date=date,
                                      price_per_hour=price_per_hour)

        obj.save()

        return redirect('Hospitals')


    return render(request,'hospital/create_job.html')

def Delete_job(request,id):
    WorkShift.objects.get(id=id).delete()
    return redirect('Hospitals')


def Accept(request,id):
    obj=ShiftApplication.objects.get(id=id)
    obj.application_status = 'ACCEPTED'
    obj.save()
    return redirect('Hospitals')

def Reject(request,id):
    obj=ShiftApplication.objects.get(id=id)
    obj.application_status = 'REJECTED'
    obj.save()
    return redirect('Hospitals')

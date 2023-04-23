from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Accounts.models import WorkShift,Nurse,ShiftApplication
from django.views.decorators.cache import cache_control
# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Nurses(request):
    try:
        obj1 = WorkShift.objects.all()
        obj2 = ShiftApplication.objects.filter(nurse = Nurse.objects.get(user=request.user))
        obj=[]
        jobs=[]
        for i in obj2:
            obj.append(i.shift)
        
        for j in obj1:
            if j not in obj:
                jobs.append(j)

    except:
        return redirect('Nurses')
    return render(request,'nurse/nurse.html',{'jobs':jobs})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Work_applied(request):
    user = request.user
    nurse = Nurse.objects.get(user=user)
    try:
        obj = ShiftApplication.objects.filter(nurse=nurse)
    except:
        return redirect()
    return render(request,'nurse/work_apply.html',{'jobs':obj})


@login_required
def Apply(request,id):
    user = request.user
    nurse = Nurse.objects.get(user=user)
    obj = ShiftApplication.objects.create(nurse=nurse,shift=WorkShift.objects.get(id=id))

    obj.save()
    
    return redirect('Nurses')
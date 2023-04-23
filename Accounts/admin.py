from django.contrib import admin
from .models import Hospital,Nurse,WorkShift,ShiftApplication,Mediator,Account_requests
# Register your models here.


admin.site.register(Mediator)
admin.site.register(Hospital)
admin.site.register(Nurse)
admin.site.register(WorkShift)
admin.site.register(ShiftApplication)
admin.site.register(Account_requests)

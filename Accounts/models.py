from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User

# Create your models here.

class Mediator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mediator = models.ForeignKey(Mediator, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class WorkShift(models.Model):
    title = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    time = models.TimeField()
    date = models.DateField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return f"{self.hospital} - {self.date} - {self.time}"


class ShiftApplication(models.Model):
    PENDING = 'PENDING'
    REJECTED = 'REJECTED'
    ACCEPTED = 'ACCEPTED'

    MY_CHOICES = [
        (PENDING, 'PENDING'),
        (REJECTED, 'REJECTED'),
        (ACCEPTED, 'ACCEPTED')
    ]

    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    shift = models.ForeignKey(WorkShift, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(choices=MY_CHOICES, max_length=200,default=PENDING)

    def __str__(self):
        return f"{self.nurse} - {self.shift}"
    


class Account_requests(models.Model):
    full_name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)

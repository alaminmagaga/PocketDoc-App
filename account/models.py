from django.db import models
from django.contrib.auth.models import AbstractUser, User


DOCTOR_SPECIALTIES = (
    ('DBT', 'Diabeties'),
    ('HRT', 'Heart'),
    ('LVR', 'Liver'),
    ('KDN', 'Kidney'),
    ('BRN', 'Brain'),
)


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.username
    

class Doctor(User):
    specialty = models.CharField(max_length=3, choices=DOCTOR_SPECIALTIES)

class Client(User):
    no_of_pred = models.IntegerField()


class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    


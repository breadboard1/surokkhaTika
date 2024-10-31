from django.db import models
from django.contrib.auth.models import User


GENDER_TYPE=[
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
]

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient/images')
    mobile_no = models.CharField(max_length=12)
    nid = models.CharField(max_length=30, unique=True)
    gender = models.CharField(choices=GENDER_TYPE, max_length=10)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

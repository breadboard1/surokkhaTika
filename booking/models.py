from django.db import models
from patient.models import Patient
from campaign.models import Campaign
from vaccine.models import Vaccine

DOSE_NUMBER=[
    ('1', 'First Dose'),
    ('2', 'Second Dose'),
    ('3', 'Third Dose'),
    ('4', 'fourth Dose'),
    ('5', 'fifth Dose'),
]

class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose_number = models.CharField(choices=DOSE_NUMBER, max_length=10)
    appointment_date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.patient} registed for {self.vaccine.name}"
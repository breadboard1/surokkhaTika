from django.db import models
from vaccine.models import Vaccine
from doctor.models import Doctor
from patient.models import Patient

CAMPAIGN_STATUS = [
    ('Planned', 'Planned'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
]

class Campaign(models.Model):
    name = models.CharField(max_length=250)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    description = models.TextField()
    target_population = models.IntegerField()
    status = models.CharField(choices=CAMPAIGN_STATUS, max_length=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=250)
    dose_per_individual = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} at {self.location}."


STAR_CHOICES=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)

    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name} reviews on {self.campaign.name}"

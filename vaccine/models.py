from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    manufacturer = models.CharField(max_length=250)
    image = models.ImageField(upload_to="vaccine/images/")

    def __str__(self):
        return f"{self.name} by {self.manufacturer}"
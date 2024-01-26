from django.db import models

# Create your models here.


class Turnover(models.Model):
    # Define your model fields
    sector = models.CharField(max_length=100, blank=True)
    turnovers = models.CharField(max_length=100, blank=True)
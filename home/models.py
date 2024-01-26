from django.db import models

# Create your models here.
class TopLooser(models.Model):
    # Define your model fields
    Symbol = models.CharField(max_length=100, blank=True)
    LTPprice = models.CharField(max_length=100, blank=True)
    PerChanges = models.CharField(max_length=100, blank=True)
    Open = models.CharField(max_length=100, blank=True)
    High = models.CharField(max_length=100, blank=True)
    Low = models.CharField(max_length=100, blank=True)
    Qty = models.CharField(max_length=100, blank=True)

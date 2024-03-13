from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from .utils import STATE_CHOICES, NEW_EXIST_CHOICES, NAICS_CHOICES, URBAN_RURAL_CHOICES, REV_LINE_CHOICES, LOW_DOC_CHOICES, REAL_ESTATE_CHOICES, MIS_STATUS_CHOICES


class User(AbstractUser):
    pass


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=False, null=False)
    zip = models.PositiveIntegerField(validators=[MaxValueValidator(99)], blank=False, null=False)
    naics = models.CharField(max_length=2, choices=NAICS_CHOICES, blank=False, null=False)
    num_employees = models.PositiveIntegerField(blank=False, null=False)
    franchise_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], blank=False, null=False)
    urban_rural = models.CharField(max_length=5, choices=URBAN_RURAL_CHOICES, blank=False, null=False)

    def __str__(self):
        return (f"{self.name}, {self.city}, {self.state}")


class Request(models.Model):
    company = models.ForeignKey("Company", on_delete=models.PROTECT, related_name="company_requests")
    date = models.DateTimeField(auto_now_add=True)
    bank = models.CharField(max_length=100, blank=False, null=False)
    bank_state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=False, null=False)
    term = models.PositiveIntegerField(validators=[MaxValueValidator(1000)], blank=False, null=False)
    new_exist = models.CharField(max_length=8, choices=NEW_EXIST_CHOICES, blank=False, null=False)
    rev_line_cr = models.CharField(max_length=1, choices=REV_LINE_CHOICES, blank=False, null=False)
    low_doc = models.CharField(max_length=1, choices=LOW_DOC_CHOICES, blank=False, null=False)
    gr_appv = models.PositiveIntegerField(blank=False, null=False)
    sba_appv = models.PositiveIntegerField(blank=False, null=False)
    real_estate = models.CharField(max_length=1, choices=REAL_ESTATE_CHOICES, blank=False, null=False)
    status = models.CharField(max_length=1, choices=MIS_STATUS_CHOICES, blank=True, null=True)

    def formatted_date(self):
        return self.date.strftime('%d/%m/%Y')
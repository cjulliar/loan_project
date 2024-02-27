from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import state_list


class User(AbstractUser):
    pass


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, choices=state_list)
    zip = models.PositiveIntegerField(max_length=2, blank=False, null=False)
    naics = models.PositiveIntegerField(max_length=2, blank=False, null=False)
    num_employees = models.PositiveIntegerField(blank=False, null=False)
    franchise_code = models.PositiveIntegerField(blank=False, null=False)
    urban_rural = models.BinaryField(blank=False, null=False)


class Request(models.Model):
    company = models.ForeignKey("Company", on_delete="PROTECT", related_name="company_requests")
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    bank = models.CharField(max_length=100)
    bank_state = models.CharField(choices=state_list)
    term = models.PositiveIntegerField()
    # num_employees = models.PositiveIntegerField(default=company_data("num_employees")) # possible changes
    new_exist = models.BinaryField()
    # franchise_code = models.PositiveIntegerField() # possible changes
    # urban_rural = models.BinaryField() # possible changes
    rev_line_cr = models.BinaryField()
    low_doc = models.BinaryField()
    gr_appv = models.PositiveIntegerField()
    sba_appv = models.PositiveIntegerField()
    # zip = models.PositiveIntegerField() # possible changes
    # naics = models.PositiveIntegerField() # possible changes
    real_estate = models.BinaryField()
    status = models.BinaryField()

    def company_data(self, column):
        company = self.company
        return company[column]
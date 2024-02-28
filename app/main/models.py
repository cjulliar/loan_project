from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import state_list, new_exist_list, urban_rural_list, rev_line_list, low_doc_list, real_estate_list, mis_status


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
    urban_rural = models.BinaryField(choices=urban_rural_list, blank=False, null=False)


class Request(models.Model):
    company = models.ForeignKey("Company", on_delete="PROTECT", related_name="company_requests")
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    bank = models.CharField(max_length=100, blank=False, null=False)
    bank_state = models.CharField(choices=state_list, blank=False, null=False)
    term = models.PositiveIntegerField(blank=False, null=False)
    # num_employees = models.PositiveIntegerField(default=company_data("num_employees")) 
    new_exist = models.CharField(choices=new_exist_list, blank=False, null=False)
    # franchise_code = models.PositiveIntegerField() 
    # urban_rural = models.BinaryField() 
    rev_line_cr = models.CharField(choices=rev_line_list, blank=False, null=False)
    low_doc = models.CharField(choices=low_doc_list, blank=False, null=False)
    gr_appv = models.PositiveIntegerField(blank=False, null=False)
    sba_appv = models.PositiveIntegerField(blank=False, null=False)
    # zip = models.PositiveIntegerField() 
    # naics = models.PositiveIntegerField() 
    real_estate = models.BooleanField(choices= real_estate_list, blank=False, null=False)
    status = models.BooleanField(choices=mis_status, blank=False, null=False)

    def company_data(self, column):
        company = self.company
        return company[column]
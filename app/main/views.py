from django.shortcuts import render
from requests import Request

# Create your views here.
def about_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def loan_history_page(request):
    return render(request, 'main/loan_history_page.html')

def loan_request_page(request):
    return render(request, 'main/loan_request_page.html')

def company_page(request, nameCompany):
    context = {"nameCompany" : nameCompany}
    return render(request, 'main/company_page.html', context=context)

def companies_page(request):
    return render(request, 'main/companies_page.html')
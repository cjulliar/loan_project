from django.shortcuts import render
from requests import Request


def home(request):
    return render(request, 'main/home_page.html')


def about(request):
    return render(request, 'main/about_page.html')


def loan_history(request):
    return render(request, 'main/loan_history_page.html')


def loan_request(request):
    return render(request, 'main/loan_request_page.html')


def company(request, nameCompany):
    context = {"nameCompany" : nameCompany}
    return render(request, 'main/company_page.html', context=context)


def companies(request):
    return render(request, 'main/companies_page.html')
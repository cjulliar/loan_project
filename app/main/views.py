import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CompanyForm, RequestForm
from .utils import api_call
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Company, Request

def home(request):
    return render(request, 'main/home_page.html')


def about(request):
    return render(request, 'main/about_page.html')


# def companies(request):
#     return render(request, 'main/companies_page.html')
class CompaniesListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = "main/companies_page.html"

# def company(request, nameCompany):
#     context = {"nameCompany" : nameCompany}
#     return render(request, 'main/company_page.html', context=context)

# class CompanyDetailView(LoginRequiredMixin, DetailView):
#     model = Company
#     template_name = "main/company_page.html"
class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "main/company_page.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context['object']
        context['company'] = company
        requests = Request.objects.filter(company=company)
        context['requests'] = requests
        return context

def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"L'entreprise {form.cleaned_data['name']} est enregistré, vous pouvez maintenant la sélectionner.")
            return HttpResponseRedirect(reverse("main:loan_request"))
        
        else:
            messages.error(request, "L'un des champs renseigné est incorrecte, veuillez réessayer.")
            return HttpResponseRedirect(reverse("main:create_company"))

    else:
        return render(request, "main/create_company_page.html", {
            "form": CompanyForm()
        })


# def loan_history(request):
#     return render(request, 'main/loan_history_page.html')
class LoanHistoryListView(LoginRequiredMixin, ListView):
    model = Request
    template_name = "main/loan_history_page.html"

def loan_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)

        if form.is_valid():

            try:
                application = form.cleaned_data

                url = "http://0.0.0.0:8042/predict"

                headers = {
                    "Accepts": "application/json",
                }

                session = Session()
                session.headers.update(headers)

                company = application["company"]

                feature_inputs = {
                'State': company.state,
                'Bank': application["bank"],
                'BankState': application["bank_state"],
                'Term': application["term"],
                'NoEmp': company.num_employees,
                'NewExist': application["new_exist"],
                'FranchiseCode': str(company.franchise_code),
                'UrbanRural': company.urban_rural,
                'RevLineCr': application["rev_line_cr"],
                'LowDoc': application["low_doc"],
                'GrAppv': application["gr_appv"],
                'SBA_Appv': application["sba_appv"],
                'Zip2': str(company.zip),
                'NAICS2': str(company.naics),
                'RealEstate': application["real_estate"]
                }

                features = json.dumps(feature_inputs)
                response = session.post(url, data=features)
                result = json.loads(response.text)
                result = result["category"]

                application = form.save()
                application.status = result
                application.save()

            except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
                messages.error(request, f"Problème survenu pendant la prédiction ({e}), veuillez réessayer.")
                return HttpResponseRedirect(reverse("main:loan_request"))          

            return render(request, "main/loan_request_page.html", {
                "application": application
            })

        else:
            messages.error(request, "L'un des champs renseigné est incorrecte, veuillez réessayer.")
            return HttpResponseRedirect(reverse("main:loan_request"))

    else:
        return render(request, 'main/loan_request_page.html', {
            "form": RequestForm()
        })
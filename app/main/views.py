import json
import os
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Company, Request
from .forms import CompanyForm, RequestForm, UserCreationFormCustom


def home(request):
    return render(request, 'main/home_page.html')


def about(request):
    return render(request, 'main/about_page.html')


class CompaniesListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = "main/companies_page.html"


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


@login_required
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


class LoanHistoryListView(LoginRequiredMixin, ListView):
    model = Request
    template_name = "main/loan_history_page.html"


@login_required
def loan_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)

        if form.is_valid():

            try:
                application = form.cleaned_data

                url = os.getenv("API_URL")

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
    

class SignupView(CreateView):
    form_class = UserCreationFormCustom
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
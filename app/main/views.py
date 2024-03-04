from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from requests import Request
from .forms import CompanyForm, RequestForm
from .utils import api_call


def home(request):
    return render(request, 'main/home_page.html')


def about(request):
    return render(request, 'main/about_page.html')


def companies(request):
    return render(request, 'main/companies_page.html')


def company(request, nameCompany):
    context = {"nameCompany" : nameCompany}
    return render(request, 'main/company_page.html', context=context)


def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"L'entreprise {form.cleaned_data["name"]} est enregistré, vous pouvez maintenant la sélectionner.")
            return HttpResponseRedirect(reverse("main:loan_request"))
        
        else:
            messages.error(request, "L'un des champs renseigné est incorrecte, veuillez réessayer.")
            return HttpResponseRedirect(reverse("main:create_company"))

    else:
        return render(request, "main/create_company_page.html", {
            "form": CompanyForm()
        })


def loan_history(request):
    return render(request, 'main/loan_history_page.html')


def loan_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)

        if form.is_valid():

            try:
                result = api_call(form.cleaned_data)
                application = form.save()
                application.status = result
                application.save()

            except:
                messages.error(request, "Problème survenu pendant la prédiction, veuillez réessayer.")
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
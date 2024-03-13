from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Company, Request


class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "password1", "password2", "email"]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        labels = {
            "name": "Nom de l'entreprise souhaitant réaliser le prêt",
            "city": "Ville où se situe l'entreprise",
            "state": "État où se situe l'entreprise",
            "zip": "Code postal de l'entreprise (deux premiers chiffres)",
            "naics": "Secteur d'activité de l'entreprise",
            "num_employees": "Nombre d'employés de l'entreprise",
            "franchise_code": "Code indiquant la franchise de l'entreprise (0 si non franchisé)",
            "urban_rural": "Type d'environnement où se situe l'entreprise",
        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['company', 'bank', 'bank_state', 'term', 'new_exist', 'rev_line_cr', 'low_doc', 'gr_appv', 'sba_appv', 'real_estate']
        labels = {
            "company": "Entreprise souhaitant réaliser le prêt",
            "bank": "Nom de la banque accordant le prêt",
            "bank_state": "État où se situe la banque",
            "term": "Durée du prêt en nombre de mois",
            "new_exist": "L'entreprise est créé depuis moins de deux ans",
            "rev_line_cr": "Ligne de crédit est renouvelable",
            "low_doc": "La demande de prêt peut être fait en 1 page",
            "gr_appv": "Montant total approuvé par la banque pour le prêt",
            "sba_appv": "Montant approuvé par la SBA pour le prêt",
            "real_estate": "Le prêt est lié à l'immobilier",
        }
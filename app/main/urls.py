from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('loan_history/', views.loan_history, name='loan_history'),
    path('loan_request/', views.loan_request, name='loan_request'),
    path('company/<str:nameCompany>', views.company, name='company'),
    path('companies/', views.companies, name='companies'),
]

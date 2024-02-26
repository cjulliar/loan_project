from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('loan_history/', views.loan_history_page, name='loan_history'),
    path('loan_request/', views.loan_request_page, name='loan_request'),
    path('company/<str:nameCompany>', views.company_page, name='company'),
    path('companies/', views.companies_page, name='companies'),
]

from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company'),
    path("create_company", views.create_company, name="create_company"),
    path('loan_history/', views.LoanHistoryListView.as_view(), name='loan_history'),
    path('loan_request/', views.loan_request, name='loan_request'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]

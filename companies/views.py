from django.shortcuts import render
from django.views.generic import ListView
from .models import Company

# Create your views here.


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'companies/company_list.html'

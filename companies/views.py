from django.shortcuts import render
from django.views.generic import ListView
from .models import Company
from django.views.generic import DetailView

# Create your views here.


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'companies/company_list.html'


class CompanyDetailView(DetailView):

    model = Company
    template_name = "companies/company_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = self.object.get_contacts()
        return context

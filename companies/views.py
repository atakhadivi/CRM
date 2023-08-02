from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Company, Contact, FollowUp
from django.views.generic import DetailView
from django.utils import timezone

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
        context['followups'] = self.object.followup_set.all()
        return context


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'


def complete_followup(request, pk):
    followup = get_object_or_404(FollowUp, pk=pk)
    followup.completed = True
    followup.save()


class OverdueFollowUpsView(ListView):

    model = FollowUp

    def get_queryset(self):
        now = timezone.now().date()
        return super().get_queryset().filter(date__lt=now)


class CompanyReport(TemplateView):

    template_name = 'reports/company_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companies = Company.objects.annotate(
            num_contacts=Count('contact')
        ).order_by('category__name', 'name')

        context['companies'] = companies
        return context


class ContactReport(ListView):

    model = Contact
    template_name = 'reports/contacts_report.html'

    def get_queryset(self):
        return super().get_queryset().order_by('company__name', 'last_name')


class OverdueFollowUpsReport(ListView):

    model = FollowUp
    template_name = 'reports/overdue_followups.html'

    def get_queryset(self):
        now = timezone.now().date()
        return super().get_queryset().filter(date__lt=now)

from django.contrib import admin
from .models import Company, Contact

admin.site.register(Company)
admin.site.register(Contact)

class ContactInline(admin.TabularInline):
    model = Contact
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        ContactInline,
    ]
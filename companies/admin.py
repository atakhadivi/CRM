from django.contrib import admin
from .models import Company, Contact, Category, FollowUp


class ContactInline(admin.TabularInline):
    model = Contact


admin.site.register(FollowUp)


class FollowUpInline(admin.TabularInline):
    model = FollowUp


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        ContactInline,
    ]
    inlines = [FollowUpInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('company',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)

    search_fields = ('name',)

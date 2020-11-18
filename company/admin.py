from django.contrib import admin
from .models import Company, Employee

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
        Configuração de company dentro do Django admin.
    """
    list_dispĺay = ('name', 'slug', 'created')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
        Configuração de funcionário dentro do Django admin.
    """
    list_dispĺay = ('user', 'bio', 'birth_date')

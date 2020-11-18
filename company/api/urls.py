from django.urls import path
from . import views

app_name = 'company'
urlpatterns = [
    #Endpoints referentes a company

    # Endpoint para criar uma empresa
    path('createcompany/', views.CompanyCreateView.as_view(), name='company_create'),

    # Endpoint para mostrar todas as empresas
    path('companies/', views.CompanyListView.as_view(), name='company_list'),

    # Endpoint para mostrar uma empresa dado seu id
    path('companies/<pk>/', views.CompanyDetailView.as_view(), name='company_detail'),


    #Endpoints referentes ao usuário

    # Endpoint para criar um usuário no sistema
    path('register/', views.registration_view, name="register"),

    # Endpoint para mostrar todos os usuários que existem no sistema
    path('users/', views.UserListView.as_view(), name="user_detail"),


    #Endpoints referentes a funcionário
    
    # Endpoint para criar um funcionário, depois de já ter um perfil de usuário para ele
    path('createemployee/', views.EmployeeCreateView.as_view(), name="employee_create"),

    # Endpoint para ver todos os funcionários do sistema
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),

    # Endpoint para ver um funcionário, dado seu username
    path('employees/<str:username>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
]

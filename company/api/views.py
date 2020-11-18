from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Company, Employee
from .serializers import CompanySerializer, CreateCompanySerializer, EmployeeSerializer, EmployeeDetailSerializer
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, EmployeeCreateSerializer, CompanyDetailSerializer, UserSerializer
from django.shortcuts import get_object_or_404


"""
    Views referentes a Company.
"""
class CompanyListView(generics.ListAPIView):
    """
        View para mostrar todas as empresas que estão cadastradas no sistema.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(generics.RetrieveAPIView):
    """
        View que é usada para mostrar detalhadamente uma empresa, junto com os
        funcionários que ela possui.
    """

    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer

class CompanyCreateView(generics.CreateAPIView):
    """
        View para criar uma empresa.
    """

    queryset = Company.objects.all()
    serializer_class = CreateCompanySerializer


"""
    Views referentes a Usuário.
"""
@api_view(['POST', ])
def registration_view(request):
    """
        View usada para criar um usuário no sistema.
    """

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['email'] = user.email
            data['username'] = user.username
            data['id'] = user.id
        else:
            data = serializer.errors
        return Response(data)

class UserListView(generics.ListAPIView):
    """
        View usada para mostrar os dados de todos os usuários que existem no
        sistema.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
    Views referentes a Funcionário.
"""
class EmployeeCreateView(generics.CreateAPIView):
    """
        View para criar um funcionário, depois de já ter um perfil de usuário
        criado para esse funcionário.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateSerializer

class EmployeeListView(generics.ListAPIView):
    """
        View usada para mostrar os empregados num geral que existem no sistema.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.ListAPIView):
    """
        View para mostrar o funcionário dado seu username, mostrando seus dados
        e as empresas que trabalha.
    """

    serializer_class = EmployeeDetailSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        username = self.kwargs['username']
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset

@api_view(['POST', ])
def create_employee_view(request):
    """
        View usada para criar um funcionário, apenas depois que o user já foi
        criado.
        NÃO ESTÁ SENDO USADA.
    """

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfullt registered a new employee.'
            data['email'] = user.email
            data['username'] = user.username
            data['id'] = user.id
        else:
            data = serializer.errors
        return Response(data)

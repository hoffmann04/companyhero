from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    """
        Modelo simples referente a uma empresa, que possui nome, slug 
        e a data de criação.
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
        Modelo de um funcionário, que extende o modelo de usuário padrão do Django. 
        Logo, um funcionário é um usuário com dados específicos de um funcionário,
        podendo adicionar mais dados nesse perfil de funcionário com facilidade.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    companies = models.ManyToManyField(Company, related_name='employees')

    def __str__(self):
        return self.user.username
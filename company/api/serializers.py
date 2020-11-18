from rest_framework import serializers
from ..models import Company, Employee
from django.contrib.auth.models import User


"""
    Serializers referentes a Company.
"""
class CompanySerializer(serializers.ModelSerializer):
    """
        Serializer para mostrar as empresas.
    """
    class Meta:
        model = Company
        fields = '__all__'

class CreateCompanySerializer(serializers.ModelSerializer):
    """
        Serializer responsável na criação da empresa, limitando os campos.
    """
    class Meta:
        model = Company
        fields = ['name', 'slug']

class CompanyDetailSerializer(serializers.ModelSerializer):
    """
        Serializer responsável por mostrar a empresa e seus empregados.
    """
    employees = serializers.StringRelatedField(many=True)

    class Meta:
        model = Company
        fields = ['name', 'slug', 'created', 'employees']


"""
    Serializers referentes a Usuário.
"""
class RegistrationSerializer(serializers.ModelSerializer):
    """
        Serializer responsável por cadastrar o usuário no sistema.
    """

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    """
        Serializer para mostrar informações do user
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


"""
    Serializers referentes a Funcionário.
"""
class EmployeeCreateSerializer(serializers.ModelSerializer):
    """
        Serializer responsável por criar um funcionário.
    """
    class Meta:
        model = Employee
        fields = ['user', 'bio', 'birth_date', 'companies']

class EmployeeSerializer(serializers.ModelSerializer):
    """
        Serializer que pega informações do funcionário.
    """
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Employee
        fields = ['id', 'user', 'bio', 'birth_date', 'companies']

class EmployeeDetailSerializer(serializers.ModelSerializer):
    """
        Serializer responsável por mostrar o funcionário e as empresas que ele
        trabalha
    """

    # username = serializers.SerializerMethodField("getUsername")
    user = UserSerializer(read_only=True)
    # user = serializers.ReadOnlyField(source='user.username')
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'user', 'bio', 'birth_date', 'companies')
        depth = 1
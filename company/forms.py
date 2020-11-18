from django import forms
from .models import Company, Employee


class CompanyForm(forms.ModelForm):
    """
        Form referente a criar uma empresa.
    """
    class Meta:
        model = Company
        fields = ['name']


class UserForm(forms.ModelForm):
    """
        Form referente a criar um usuário.
    """
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Senha',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Senhas não são iguais.')
        return cd['password2']


class EmployeeForm():
    """
        Form referente a criar um funcionário.
    """
    class Meta:
        model = Employee
        fields = ['bio', 'birth_date', 'companies']
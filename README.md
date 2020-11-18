# Company Hero Test

## Descrição:

Esta é uma pequena aplicação que tem como objetivo a criação de empresas e funcionários. Os funcionários são também usuários dentro dessa aplicação.

A aplicação também fornece endpoints para criação (POST) e consulta (GET) de empresas e de funcionários. Não foram desenvolvidos endpoints para update (PUT) e exclusão (DELETE).

O código está devidamente comentado, mas caso surja alguma dúvida, fique a vontade para entrar em contato comigo :)

## Abordagem e Implementação:

A abordagem para realizar essa tarefa foi a criação de um modelo para empresa, no código chamado de Company, e um modelo para o funcionário, no código chamado de Employee.

Abaixo temos o código de Company:

```
class Company(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

Devido a um funcionário também ter que ser um usuário da plataforma, foi escolhido extender o modelo padrão de usuário do Django, User. Logo, um funcionário é um usuário, ou seja, contém os atributos do User (username, email, first_name, last_name, etc), e também atributos de seu próprio modelo, que podem ser adicionados a vontade. Nesse caso, funcionário também tem os campos bio (de biografia), birth_date e companies (para guardar as empresas que esse funcionário trabalha). Companies sendo um campo ManyToMany referente a Company.

Abaixo temos o código de Employee:

```
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    companies = models.ManyToManyField(Company, related_name='employees')

    def __str__(self):
        return self.user.username
```

Foram criados também formulários para a criação de uma empresa, de um usuário e de um funcionário. Todos estes formulários estão no arquivo forms.py e devidamente comentados.

## Endpoints:

Para essa pequena API foram criados os seguintes endpoints:

| Endpoint               | Função                    | Método  | JSON                                                               |
|------------------------|---------------------------|---------|--------------------------------------------------------------------|
| Referentes a uma Empresa: |
|/api/createcompany/     | Criar uma empresa         | POST    | {"name":"Nome da Empresa", "slug":"nome-da-empresa"}               |
|/api/companies/         | Mostra todas as empresas  | GET     |            |
|/api/companies/pk/    | Dado o id de uma empresa, mostra os seus dados e seus funcionários         | GET    |    |
| Referentes a um Usuário: |
|/api/register/     | Criar um Usuário         | POST    | {"email":"email@email.com", "username":"userteste", "password":senha, "password2":senha, "first_name": "Nome", "last_name": "Sobrenome"}               |
|/api/users/     | Retorna todos os Usuários do sistema         | GET    |                |
| Referentes a um Funcionário: |
|/api/createemployee/     | Criar um Funcionário         | POST    | {"user":user_id, "bio":"Biografia do funcionário", "birth-date":"AAAA-MM-DD", "companies": lista contendo ids das empresas}               |
|/api/employees/     | Retorna todos os Funcionários do sistema         | GET    |                |
|/api/employees/username/     | Retorna informações de um Funcionário dado seu username         | GET    |               |

## Como usar:

A aplicação foi publicada no Heroku, podendo ser acessada pelo link:

https://companyheroteste.herokuapp.com/

Se ocorrer demora, é devido ao Heroku colocar em modo de espera uma aplicação que não está sendo usada no momento.

Como a alicação é focada na sua API, nenhuma página retornará se o link acima for acessado, logo, é preciso ter em mente que essa aplicação só funcionará se algum dos endpoints acima for usado, por exemplo:

https://companyheroteste.herokuapp.com/api/companies/

Esse link retornará todas as empresas cadastradas no sistema.

### Importante:
A aplicação no Heroku está apenas com uma empresa cadastrada, e um superusuário, logo, precisará ser cadastrado algumas empresas, usuários e funcionários para os endpoints de GET retornarem dados.

### O que fazer:
1. Primeiramente, deve-se cadastrar empresas
2. Depois, devemos cadastrar um usuário, vale lembrar que para criar um funcionário, precisaremos do id desse usuário que foi criado. Esse id é retornado na resposta após a criação do user, ou também pode ser pego usando o endpoint /api/users/
3. Apenas depois de cadastrarmos um usuário é que podemos criar um funcionário
4. Depois disso, já teremos dados a serem retornados nos endpoints de GET :D

#### p.s.: Caso necessário, O Django admin é acessado normalmente em /admin o superuser já existente se chama hero e a senha é herocompany

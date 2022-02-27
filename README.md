## User Registration

Projeto criado para pôr em prática meus conhecimentos. Nesse projeto é possível cadastrar um usuário, listar todos os usuários cadastrados mostrando apenas informações restritas. Também é possível mostrar um usuário, a partir do seu id, com todas as informações deste usuário e listar todos os usuários por cep.

## Instalação

- Primeiro faça o fork e clone o repositório

```
git clone git@github.com:MiqueiasCS/userRegister_back.git
```

- Crie o ambiente um ambiente [virtual em python](https://docs.python.org/pt-br/3/tutorial/venv.html)

```
$ python -m venv venv --upgrade-deps
```

- Entre no ambiente virtual

```
$ source venv/bin/activate
```

- Instale as dependencias no arquivo `requirements.txt`

```
$ pip install -r requirements.txt
```

- Crie um arquivo `.env` e configure as variáveis **FLASK_ENV**, **SECRET_KEY** e **SQLALCHEMY_DATABASE_URI** seguindo o exemplo do arquivo `.env.example`
  - Crie um banco de dados no PostgreSQL e configure SQLALCHEMY_DATABASE_URI com as informações do banco (nome do banco, usuário,senha);
  - SECRET_KEY pode ser qualquer palavra. Ela será usada para criar o token;
  - FLASK_ENV indica o ambiente de desenvolvimento (Environment).
- Crie as tabelas no banco de dados através do comando:

```
$ flask db upgrade
```

- Inicie a aplicação local através do comando:

```
$ flask run
```

- A aplicação inicializará na rota http://127.0.0.1:5000/. Você deverá ver algo semelhante ao snippet logo abaixo no seu terminal:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 380-161-167
```

## (opcional) Rodando o banco de dados em um container

- Você também pode rodar o PostgreSQL em um container do docker. Para isso adicione as seguintes variáveis ao arquivo _.env_ conforme o exemplo dado em _.env.example_:

  - POSTGRES_DB
  - POSTGRES_USER
  - POSTGRES_PASSWORD

- Execute o seguinte comando para criar e rodar o container:

```
docker-compose up
```

- Crie as tabelas no banco de dados do container através do comando:

```
$ flask db upgrade
```

- Inicie a aplicação local através do comando:

```
$ flask run
```

- A aplicação inicializará na rota http://127.0.0.1:5000/

- Para encerrar o container use:

```
docker-compose down
```

- #### Obs: ao encerrar o container todos os dados gravados no banco de dados do mesmo serão perdidos.

#

## Tecnologias usadas

- Python
- Flask
- SQALAlchemy
- Postgresql
- Docker

## Rotas

### Base Url: http://127.0.0.1:5000/api

## POST /user

- Registra um usuário
- body
  - apenas a chave "complement" é opcional.

```python
   # exemplo
   {
	    "name":"fulano",
	    "email":"fulano@mail.com",
	    "password":"123456",
	    "cep":"11111-111",
	    "city":"Fortaleza",
	    "district": "Barroso",
	    "street":"R Manuel Figueiredo",
	    "House_number":222,
            "complement":"A"
   }

```

- response:
- _RESPONSE STATUS -> HTTP **201 (CREATED)**_

```python
   # exemplo
   {
  	"id": 1,
  	"name": "fulano",
  	"email": "fulano@mail.com",
  	"address": {
    		"cep": "11111-111",
    		"city": "Fortaleza",
    		"district": "Barroso",
    		"street": "R Manuel Figueiredo",
    		"House_number": 222,
    		"complement": "A"
  		}
  }

```

- **Requisições inválidas**

- _RESPONSE STATUS -> HTTP **400 (BAD REQUEST)**_
- sem uma das chaves não opcionais:

```python
# - exemplo:

# Body
{

    "email":"fulano@mail.com",
    "password":"123456",
    "cep":"11111-111",
    "city":"Fortaleza",
    "district": "Barroso",
    "street":"R Manuel Figueiredo",
    "House_number":222,
    "complement":"A"
}
```

```python
# Response
{
  "message": "One or more mandatory keys is missing",
  "expected": [
        "name",
        "email",
        "password",
        "cep",
        "city",
        "district",
        "street",
        "House_number"
    ],
  "received": [
        "email",
        "password",
        "cep",
        "city",
        "district",
        "street",
        "House_number",
        "complement"
    ]
}
```

- _RESPONSE STATUS -> HTTP **400 (BAD REQUEST)**_
- Passar chaves com valor errado:

```python
# - exemplo:

# Body
{
    "name":"fulano",
    "email":1234,
    "password":"123456",
    "cep":"11111-111",
    "city":"Fortaleza",
    "district": "Barroso",
    "street":"R Manuel Figueiredo",
    "House_number":222,
    "complement":"A"
}
```

```python
# Response
{
  "message": "One or more keys have the wrong type value",
  "expected": {
    "name": "string",
    "email": "string",
    "password": "string",
    "cep": "string",
    "city": "string",
    "district": "string",
    "street": "string",
    "House_number": "integer"
  },
  "received": {
    "name": "string",
    "email": "integer",
    "password": "string",
    "cep": "string",
    "city": "string",
    "district": "string",
    "street": "string",
    "House_number": "integer",
    "complement": "string"
  }
}
```

- _RESPONSE STATUS -> HTTP **409 (CONFLICT)**_
  - tentar cadastrar um email já registrado

```python
# Response
{
  "message": "email already exists"
}
```

- _RESPONSE STATUS -> HTTP **400 (BAD REQUEST)**_
  - passar um cep com formato diferente de xxxxx-xx

```python
# Response
{
  "message": "Invalid Cep"
}
```

## POST /login

- Faz o login do usuário cadastrado
- body

```python
{
  "email":"fulano@mail.com",
  "password":"123456"
}
```

- response
  - _RESPONSE STATUS -> HTTP **200(OK)**_

```python
{
  "acess_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NTkxOTY4NCwianRpIjoiNzFlMjAzODItOTMxMC00Zjc0LWExZmItMzQwYmYxZmY3MDEyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwiZW1haWwiOiJmdWxhbm9AbWFpbC5jb20ifSwibmJmIjoxNjQ1OTE5Njg0LCJleHAiOjE2NDU5MjA1ODR9.1f1_uEMO3wX-NieGoSNVqqhYb4NftiMooMH5w-T0pJo"
}
```

- **Requisições inválidas**

- _RESPONSE STATUS -> HTTP **404 (NOT FOUND)**_

```python
# Response
{
  "email": "fulasno@mail.com",
  "message": "Email Not registered"
}
```

- _RESPONSE STATUS -> HTTP **401 (UNAUTHORIZED)**_

```python
{
  "message": "email and password do not match"
}
```

## GET /user

- Lista todos os usuários

- response:
  - _RESPONSE STATUS -> HTTP **200(OK)**_

```python
# response
[
    {
    "id": 6,
    "name": "fulano",
    "email": "fulano@mail.com",
    }
]
```

## GET /user/< id >

- Mostra um único usuário a partir do deu id
- Necessário **token (Authorization Bearer)**;
- response:
- _RESPONSE STATUS -> HTTP **200(OK)**_

```python
# response
{
  "id": 6,
  "name": "fulano",
  "email": "fulano@mail.com",
  "address": {
    "cep": "11111-111",
    "city": "Fortaleza",
    "district": "Barroso",
    "street": "R Manuel Figueiredo",
    "House_number": 222,
    "complement": "A"
  }
}
```

- **Requisições inválidas**
- _RESPONSE STATUS -> HTTP **401 (UNAUTHORIZED)**_
  - Fazer requisição sem o token

```python
# Response
{
  "msg": "Missing Authorization Header"
}
```

- _RESPONSE STATUS -> HTTP **404 (NOT FOUND)**_
  - passar id não existente como parâmetro

```python
# Response
{
  "message": "User not found"
}
```

## GET /user/cep/< cep >

- Mostra uma lista de usuários que possuem o mesmo CEP.
- Necessário **token (Authorization Bearer)**;
- response:
- _RESPONSE STATUS -> HTTP **200(OK)**_

```python
[
  {
    "user": {
      "id": 1,
      "name": "fulano",
      "email": "fulano@mail.com"
    },
    "address": {
      "city": "Fortaleza",
      "district": "Barroso",
      "street": "R Manuel Figueiredo",
      "house_number": 222,
      "complement": "A"
    }
  }
]
```

- **Requisições inválidas**
- _RESPONSE STATUS -> HTTP **400 (BAD REQUEST)**_

```python
# Response
{
  "message": "Invalid Cep"
}
```

## Contato

- [Linkedin](https://www.linkedin.com/in/miqueias-carvalho-dos-santos/)

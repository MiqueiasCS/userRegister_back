## Instalação

- Primeiro faça o fork do repositório

```

```

- Em seguida faça um git clone para a sua maquina

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

- Configure as variáveis **FLASK_ENV** e **SQLALCHEMY_DATABASE_URI** segundo o arquivo `.env.example`

  - Não esqueça de criar o seu banco de dados e adicionar no .env

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
 * Debugger PIN: 112-925-941
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

- #### Obs: ao encerrar o container todos os dados gravados no banco de dados dele serão perdidos.

#

## Tecnologias usadas

- Python
- Flask
- SQALAlchemy
- Postgresql
- Docker

## Rotas

### baseUrl: http://127.0.0.1:5000/api

#### POST /user

- Registra um usuário
- body
  - apenas a chave "complement" é opcional.

```python
   # exemplo
   {
	    "name":"fulano",
	    "email":"fulano@mail.com",
	    "password":"123456",
	    "cep":"11111111",
	    "city":"Fortaleza",
	    "district": "Barroso",
	    "street":"R Manuel Figueiredo",
	    "House_number":222,
        "complement":"A"
   }

```

- response:

```python
   # exemplo
   {
        "id": 6,
        "name": "fulano",
        "email": "fulano@mail.com",
        "cep": "11111111",
        "city": "Fortaleza",
        "district": "Barroso",
        "street": "R Manuel Figueiredo",
        "House_number": 222,
        "complement": "A"
    }

```

- **Requisições inválidas**

- _RESPONSE STATUS -> HTTP 400 (BAD REQUEST)_
- sem uma das chaves não opcionais:

```python
# - exemplo:

# Body
{

    "email":"fulano@mail.com",
    "password":"123456",
    "cep":"11111111",
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

- _RESPONSE STATUS -> HTTP 400 (BAD REQUEST)_
- Passar chaves com valor errado:

```python
# - exemplo:

# Body
{
    "name":"fulano",
    "email":1234,
    "password":"123456",
    "cep":"11111111",
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

- _RESPONSE STATUS -> HTTP 409 (CONFLICT)_
  - tentar cadastrar um email já registrado

```python
# Response
{
  "message": "email already exists"
}

```

#### GET /user

- Lista todos os usuários
- response:

```python
# response
[
    {
    "id": 6,
    "name": "fulano",
    "email": "fulano@mail.com",
    "cep": "11111111",
    "city": "Fortaleza",
    "district": "Barroso",
    "street": "R Manuel Figueiredo",
    "House_number": 222,
    "complement": "A"
    }
]
```

#### GET /user/< id >

- Mostra um único usuário a partir do deu id
- response:

```python
# Body
{
  "id": 6,
  "name": "fulano",
  "email": "fulano@mail.com",
  "cep": "11111111",
  "city": "Fortaleza",
  "district": "Barroso",
  "street": "R Manuel Figueiredo",
  "House_number": 222,
  "complement": "A"
}
```

- **Requisições inválidas**
- _RESPONSE STATUS -> HTTP 404 (NOT FOUND)_
  - passar id não existente como parâmetro

```python
# Response
{
  "message": "User not found"
}
```

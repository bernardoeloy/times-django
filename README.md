#  Times de Futebol — Django

Projeto web desenvolvido com Django para cadastro e visualização de times de futebol.

##  Tecnologias utilizadas

- Python 3.14
- Django 6.0.3
- SQLite
- HTML + CSS

##  Funcionalidades

- Cadastro de times pelo painel Admin do Django
- Listagem de times em página web
- Filtro e busca no painel Admin

##  Como rodar o projeto

**1. Clone o repositório:**
```bash
git clone https://github.com/bernardoeloy/times-django.git
```

**2. Ative o ambiente virtual:**
```bash
.\venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install django
```

**4. Rode as migrations:**
```bash
python manage.py migrate
```

**5. Crie um superusuário:**
```bash
python manage.py createsuperuser
```

**6. Inicie o servidor:**
```bash
python manage.py runserver
```

##  Acesso

| Página | URL |
|--------|-----|
| Lista de Times | http://127.0.0.1:8000 |
| Admin | http://127.0.0.1:8000/admin |

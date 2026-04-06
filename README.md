⚽ Times de Futebol — Django
Projeto web desenvolvido com Django para cadastro e visualização de times de futebol.
🛠️ Tecnologias utilizadas

Python 3.14
Django 6.0.3
SQLite
HTML + CSS

📋 Funcionalidades

Cadastro de times pelo painel Admin do Django
Listagem de times em página web
Filtro e busca no painel Admin

🗂️ Estrutura do Projeto
Projeto web/
├── venv/
└── web/
    ├── manage.py
    ├── Projeto/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── web/
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── admin.py
        └── templates/
            └── web/
                └── times.html
⚙️ Como rodar o projeto
1. Clone o repositório:
bashgit clone https://github.com/bernardoeloy/times-django.git
2. Ative o ambiente virtual:
bash# Windows
.\venv\Scripts\activate
3. Instale as dependências:
bashpip install django
4. Rode as migrations:
bashpython manage.py migrate
5. Crie um superusuário:
bashpython manage.py createsuperuser
6. Inicie o servidor:
bashpython manage.py runserver
🌐 Acesso
PáginaURLLista de Timeshttp://127.0.0.1:8000Adminhttp://127.0.0.1:8000/admin
👤 Autor
Desenvolvido por Eloy
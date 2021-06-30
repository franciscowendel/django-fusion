# django-fusion-web-page

Just a little web page called Fusion built using Django and Django REST Framework in it.

Como executar o projeto:

1. Caso não tenha o pipenv instalado:
```console
pip install pipenv
pipenv sync -d
```
2. Caso tenha o pipenv instalado:
```console
pipenv sync -d
```

3. Crie o arquivo .env e adicione as seguintes variáveis de ambiente:

- DEBUG = True
- ALLOWED_HOSTS=localhost,127.0.0.1
- SECRET_KEY='nomedachavedesejada'

4. Fazer as migrações necessárias para o projeto funcionar:
- Execute o shell do pipenv:
```console
pipenv shell
```
- Faça as migrações:
```console
python manage.py makemigrations

python manage.py migrate
```

5. Criar um superusuário:

- Execute o shell do pipenv:

```console
pipenv shell
```
- Crie o superusuário:
```console
python manage.py createsuperuser
```

6. Rodar o servidor:
- Execute o shell do pipenv:
```console
pipenv shell
```

- Rode o servidor:
```console
python manage.py runserver
```

7. Entrar no admin do projeto:
- http://127.0.0.1:8000/admin/

8. Use o projeto 
(estou levando em consideração que você já tenha um conhecimento prévio e, 
por esse motivo, não dei explicações de como acessar a API dos dados!)

[![Build Status](https://travis-ci.com/franciscowendel/django-fusion-web-page.svg?branch=main)](https://travis-ci.com/franciscowendel/django-fusion-web-page)
[![Updates](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/shield.svg)](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/)
[![Python 3](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/python-3-shield.svg)](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/)

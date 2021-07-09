# django-fusion-web-page

_A web page called Fusion built using Django; and to work with API I use Django REST Framework._

**Como executar o projeto**:

1. Caso não tenha o _pipenv_ instalado:
```console
pip install pipenv
pipenv sync -d
```

<br>

2. Caso tenha o _pipenv_ instalado:
```console
pipenv sync -d
```

<br>

3. Crie o arquivo _.env_ e adicione as seguintes variáveis de ambiente:

- DEBUG = True
- ALLOWED_HOSTS=localhost,127.0.0.1
- SECRET_KEY='nomedachavedesejada'

<br>

4. Fazer as migrações necessárias para o projeto funcionar:

- Execute o _shell_ do _pipenv_:
```console
pipenv shell
```
- Faça as migrações:
```console
python manage.py makemigrations

python manage.py migrate
```

<br>

5. Criar um superusuário:

- Execute o _shell_ do _pipenv_:

```console
pipenv shell
```
- Crie o superusuário:
```console
python manage.py createsuperuser
```

<br>

6. Rodar o servidor:
- Execute o _shell_ do _pipenv_:
```console
pipenv shell
```

- Rode o servidor:
```console
python manage.py runserver
```

<br>

7. Entrar no admin do projeto:
- http://127.0.0.1:8000/admin/

<br>

8. Use o projeto 
(estou levando em consideração que você já tenha um conhecimento prévio e, 
por esse motivo, não dei explicações de como acessar a _API_ dos dados!)

<br>

[![Build Status](https://travis-ci.com/franciscowendel/django-fusion-web-page.svg?branch=main)](https://travis-ci.com/franciscowendel/django-fusion-web-page)
[![Updates](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/shield.svg)](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/)
[![Python 3](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/python-3-shield.svg)](https://pyup.io/repos/github/franciscowendel/django-fusion-web-page/)

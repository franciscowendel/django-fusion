# Django Fusion

A page called __Fusion__ with Django as the backend and the Django Rest Framework for the API.

**How execute the project:**

1. Install all dependencies for the project to work:
```pip
pip install -r requirements.txt
```

<br>

2. Create the file **.env** and the variables below:
- DEBUG = True
- ALLOWED_HOSTS = localhost,127.0.0.1
- SECRET_KEY = 'yourkey'

<br>

3. Make the necessary migrations for the project:
```sudo
python manage.py makemigrations
```
```sudo
python manage.py migrate
```

<br>

4. Create a superuser:
```sudo
python manage.py createsuperuser
```

<br>

5. Run the server:
```sudo
python manage.py runserver
```

<br>

6. Login to the admin:
- http://127.0.0.1:8000/admin/

<br>

7. API URLs of the project:
- All the services: http://127.0.0.1:8000/api/v1/services
- Especific service: http://127.0.0.1:8000/api/v1/services/1

- All roles: http://127.0.0.1:8000/api/v1/roles
- Especific role: http://127.0.0.1:8000/api/v1/roles/1

- All employees: http://127.0.0.1:8000/api/v1/employees
- Especific employee: http://127.0.0.1:8000/api/v1/employees/1

- All features: http://127.0.0.1:8000/api/v1/features
- Especific feature: http://127.0.0.1:8000/api/v1/features/1

- All employees of an especific role: http://127.0.0.1:8000/api/v1/roles/1/employees
- An especific employee of an especific role: http://127.0.0.1:8000/api/v1/roles/1/employees/1

<br>


8. Use the project (I did not describe how to access the data API because 
I assumed you already knew this stuff!)

<br>

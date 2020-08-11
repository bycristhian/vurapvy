# API Vurapy
#
#### ¿What is Vurapy?

> Vurapy is a social network for programmers where you can interact with the entire community of people passionate about technology and programming.


### Dependencies
- Python > 3.0
- Django >= 3.0
- Database: PostgreSQL

### Installation

Remember to create and configure the parameters of local enviroment in file ```.env``` into ```vurapy/config/```:

```sh
DEBUG=True

SECRET_KEY=

ALLOWED_HOSTS=*

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
- We are using django-environ for local enviroment

#### Linux:
```sh
1. python3 -m venv .env
2. source .env/bin/activate
3. pip install -r requirements.txt 
4. python manage.py migrate
5. python manage.py runserver
```
#### Windows:
```sh
1. python -m venv .env
2. cd .env/Scripts/
3. activate
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py runserver
```
#
Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```
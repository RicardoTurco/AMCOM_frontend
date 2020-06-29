# [AMCOM] Frontend
This project is the "frontend application" to consume the "[AMCOM] Backend API".   
```
Swagger of API: 
https://amcomapi.herokuapp.com/api/v1/docs
```

## Deploy

This frontend application was deployed on Heroku:
```
https://movbancariasamcom.herokuapp.com/
```
## BD - Firebase

For data storage, the Firebase database is used.  

## Installing

To install and execution this application in your local machine, you will need to:  
(OBS: First, you need to make sure that the API is running in your local machine too.)

```
git clone https://github.com/RicardoTurco/AMCOM_frontend.git && cd AMCOM_frontend

Create and activate one "virtualenv"
(using any valid form) 


pip install -r requirements.txt


(Your need export your environment variables)
In Linux SO:
export SECRET_KEY='+_!o_!cv^2xbvsgqo@1(ivm%l73uc54c0lhl%8=b@(&j@4)bc7'
export DEBUG=True
export URL_API='http://127.0.0.1:5000/api/v1/'
(check the API URL ...)

In Windows SO:
set SECRET_KEY='+_!o_!cv^2xbvsgqo@1(ivm%l73uc54c0lhl%8=b@(&j@4)bc7'
set DEBUG=True
set URL_API='http://127.0.0.1:5000/api/v1/'
(check the API URL ...)


(The commands below are only for creating the database locally  
and not displaying error messages.)
python manage.py makemigrations
python manage.py migrate


python manage.py runserver
```

## Project Structure

This project have a basic Django Structure
```
.
├── amcom
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── transacoes
│   ├── migrations
│   │   └── __init__.py
│   ├── static
│   │   ├── transacoes
│   │   │   ├── css
│   │   │   │   ├── bootstrap.css
│   │   │   │   ├── bootstrap.css.map
│   │   │   │   ├── bootstrap.min.css
│   │   │   │   ├── bootstrap.min.css.map
│   │   │   │   ├── bootstrap.theme.css
│   │   │   │   ├── bootstrap.theme.css.map
│   │   │   │   ├── bootstrap.theme.min.css
│   │   │   │   └── bootstrap.theme.min.css.map
│   │   │   ├── fonts
│   │   │   │   ├── gluphicons-halflings.regular.eot
│   │   │   │   ├── gluphicons-halflings.regular.svg
│   │   │   │   ├── gluphicons-halflings.regular.ttf
│   │   │   │   ├── gluphicons-halflings.regular.woff
│   │   │   │   └── gluphicons-halflings.regular.woff2
│   │   │   ├── js
│   │   │   │   ├── bootstrap.js
│   │   │   │   ├── bootstrap.min.js
│   │   │   │   └── npm.js
│   ├── templates
│   │   │   ├── transacoes
│   │   │   │   ├── base.html
│   │   │   │   ├── conta_new.html
│   │   │   │   ├── conta_v.html
│   │   │   │   ├── contas.html
│   │   │   │   ├── index.html
│   │   │   │   ├── pessoa_new.html
│   │   │   │   ├── pessoa_v.html
│   │   │   │   ├── pessoas.html
│   │   │   │   ├── tipo_conta_new.html
│   │   │   │   ├── tipo_contas.html
│   │   │   │   ├── tipo_transacao_new.html
│   │   │   │   ├── tipo_transacoes.html
│   │   │   │   └── transacao.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
├── .env
├── .env_PROD
├── .gitignore
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── runtime.txt

```

### Folders

* `amcom` - The "project folder" with configurations of project.
* `transacoes` - The "app folder", contain the "resources" of project (static files, templates HTML, etc ...).
* `transacoes/static` - Static files of project(CSS and JS files).
* `transacoes/templates` - The HTML files (templates) of project.

### Files

* `.env` - The environment variables of project in DEVELOPMENT Environment.
* `.env_PROD` - The environment variables of project for PRODUCT Environment (for deploy in Heroku).
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `manage.py` - A command-line utility of Django .
* `Procfile` - Configuration of gunicorn (for deploy on Heroku).
* `README.md` - Instructions and informations of this "challenge".
* `requirements.txt` - All project dependencies (for PRODUCTION environment).
* `requirements-dev.txt` - All project dependencies (for DEVELOPMENT environment).
* `runtime.py` - Set version of Python for deploy on Heroku.



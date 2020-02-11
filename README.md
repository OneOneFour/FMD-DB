# FMD Database
## Installation
To setup this project and develop you will need to install Python >= 3.7.
Once installed the dependencies for this project can be installed by running: 
```bash
pip install -r requirements.txt
```
The following will install the Django web framework along with other dependencies.

## Running the project
Before running the project for the first time, a database must be created and migrations made. By default SQLite3 is used as the default database, which will create a db file in the root folder. For deployment MySQL or another database can be used by by changing the ```DATABASES``` variable in settings.py file. More details can be found at: [https://docs.djangoproject.com/en/3.0/ref/databases/]

In order to initialize the database run:
```bash
    python manage.py makemigrations
    python manage.py migrate
```
In order to edit the database, a superuser must be created on the site. This can be done by running
```bash
    python manage.py createsuperuser
```
Once the above is done the server can be launched by running
```bash
    python manage.py runserver
```
By default this will create the server on port 8000 at the localhost.
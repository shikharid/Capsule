### Setup Instructions
* pip install -r requirements.txt
* Create database and add details in local_settings.py folder.
* Configure redis and celery
* Run:  python manage.py makemigrations
* Run: python manage.py migrate
* Run celery server: celery -A webapp worker -l info
* Run redis server
* Run server: python manage.py runserver

### Tech Stack:
* Django==1.8
* psycopg2==2.5.4
* djangorestframework==3.3.2
* PostgreSQL
* Angular JS - 1.4.7
* Restangular
* Redis 2.8
* Celery 3.1

	##### UI Stack: 
    * Angular Material - 1.1.0-RC4
    * Materialize
    * CSS3
    * HTML5

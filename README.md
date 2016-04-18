1.pip install -r requirements.txt
2.Create database and add details in local_settings.py folder.
3.Configure redis and celery
4.Run:  python manage.py makemigrations
5.Run: python manage.py migrate
6.Run celery server: celery -A webapp worker -l info
7.Run redis server
8.Run server: python manage.py runserver
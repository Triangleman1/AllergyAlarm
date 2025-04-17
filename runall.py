from setupSettings import setupSettings
setupSettings()
import os
from django.contrib.auth.models import User

os.system("python manage.py collectstatic")
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
if not User.objects.filter(username='username').exists():
    User.objects.create_superuser('username', 'fakeemail@gmail.com', 'allergyalarm')
os.system("python manage.py runserver")
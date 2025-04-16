#DO NOT USE THIS FILE ONCE ACTUAL DATA IS IN HERE - JUST FOR TESTING
from setupSettings import setupSettings
setupSettings()
from allergy_alarm_app.models import UserExtension
from django.contrib.auth.models import User

#Clear database
User.objects.all().delete()

#if not User.objects.filter(username='username').exists():
User.objects.create_superuser('username', 'fakeemail@gmail.com', 'allergyalarm')

user = User.objects.create_user(username='user1', password='password')
user.save()
User.objects.all()
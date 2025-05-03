#DO NOT USE THIS FILE ONCE ACTUAL DATA IS IN HERE - JUST FOR TESTING
from setupSettings import setupSettings
setupSettings()
from django.contrib.auth.models import User

#Clear database
User.objects.all().delete()
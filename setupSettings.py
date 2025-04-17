import django
import os
def setupSettings():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'allergy_alarm.settings')
    django.setup()
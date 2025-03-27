from django.contrib import admin

from .models import UserIdentification, Temperature, HeartRate, Accelerometer, Gyroscope
# Register your models here.
admin.site.register(UserIdentification)
admin.site.register(Temperature)
admin.site.register(HeartRate)
admin.site.register(Accelerometer)
admin.site.register(Gyroscope)
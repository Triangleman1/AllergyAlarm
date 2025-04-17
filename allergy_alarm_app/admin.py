from django.contrib import admin

from .models import UserExtension, Temperature, HeartRate, Accelerometer, Gyroscope
# Register your models here.
admin.site.register(UserExtension)
admin.site.register(Temperature)
admin.site.register(HeartRate)
admin.site.register(Accelerometer)
admin.site.register(Gyroscope)
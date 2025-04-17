from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#user.extension should refer to this table
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    test = models.TextField(default="Default text")

    def __str__(self):
        return f"{self.user.username}"
    
# Turns out this was done automatically - still a good snippet to save
#  @receiver(post_save, sender=User)
# def extend_user(sender, instance, **kwargs):
#     u = UserExtension(user = instance, test = "test1") 
#     u.save()

class Temperature(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.FloatField()

    def __str__(self):
        return f"At {self.datetime} {self.user} recorded temperature {self.temperature}"
    
class HeartRate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    ECG = models.IntegerField()

    def __str__(self):
        return f"At {self.datetime} {self.user} recorded ECG: {self.ECG}"
    
class Accelerometer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f"At {self.datetime} {self.user} recorded acceleration x: {self.x}, y:{self.y}, z:{self.z}"
    
class Gyroscope(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f"At {self.datetime} {self.user} recorded rotational acceleration x: {self.x}, y:{self.y}, z:{self.z}"

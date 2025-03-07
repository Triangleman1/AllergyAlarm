from django.db import models

# Create your models here.
class UserData(models.Model):
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.IntegerField()
    heart_rate = models.IntegerField()

    def __str__(self):
        return f"Date/Time: {self.datetime}, temp: {self.temperature}, heart rate:{self.heart_rate}"

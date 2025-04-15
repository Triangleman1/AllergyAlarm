from django.db import models

class UserIdentification(models.Model):
    username = models.TextField()
    #An implicit primary key column is automatically created. All ForeignKeys to this table refer to this column.

    def __str__(self):
        return f"{self.username}"

class Temperature(models.Model):
    userID = models.ForeignKey(UserIdentification, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.IntegerField()

    def __str__(self):
        return f"{self.datetime}: {self.userID} recorded temperature {self.temperature}"
    
class HeartRate(models.Model):
    userID = models.ForeignKey(UserIdentification, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    ECG = models.IntegerField()

    def __str__(self):
        return f"{self.datetime}: {self.userID} recorded ECG: {self.ECG}"
    
class Accelerometer(models.Model):
    userID = models.ForeignKey(UserIdentification, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return f"{self.datetime}: {self.userID} recorded acceleration x: {self.x}, y:{self.y}, z:{self.z}"
    
class Gyroscope(models.Model):
    userID = models.ForeignKey(UserIdentification, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return f"{self.datetime}: {self.userID} recorded rotational acceleration x: {self.x}, y:{self.y}, z:{self.z}"

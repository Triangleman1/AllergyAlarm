#DO NOT USE THIS FILE ONCE ACTUAL DATA IS IN HERE - JUST FOR TESTING
from setupSettings import setupSettings
setupSettings()
from allergy_alarm_app.models import *
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
import random
import numpy as np

#Clear database
User.objects.all().delete()

#Create superuser (not important for test, just good to have)
User.objects.create_superuser('username', 'fakeemail@gmail.com', 'allergyalarm')

#Create 2 users
user1 = User.objects.create_user(username='user1', password='password')
user1.save()
user2 = User.objects.create_user(username='user2', password='password')
user2.save()
print(User.objects.all())

#HeartRate: Manual Test Cases
time = datetime.now()
rounded_time = time - timedelta(microseconds=time.microsecond)
a = HeartRate(user = user1, datetime = rounded_time, ECG = 70) 
a.save()
b = HeartRate(user = user1, datetime = rounded_time-timedelta(minutes=24), ECG = 100) #minutes test
b.save()
c = HeartRate(user = user1, datetime = rounded_time-timedelta(hours=2), ECG = 130) 
c.save()
d = HeartRate(user = user2, datetime = rounded_time-timedelta(hours=5), ECG = 0) #user2 test
d.save()
d2 = HeartRate(user = user2, datetime = rounded_time-timedelta(hours=6), ECG = 0) #user2 test
d2.save()
d3 = HeartRate(user = user2, datetime = rounded_time-timedelta(hours=7), ECG = 0) #user2 test
d3.save()
e = HeartRate(user = user1, datetime = rounded_time-timedelta(hours=13), ECG = 120) 
e.save()
f = HeartRate(user = user1, datetime = rounded_time-timedelta(hours=25), ECG = 92) #Day test (should not appear)
f.save()
g = HeartRate(user = user1, datetime = rounded_time-timedelta(days=3), ECG = 30) #Week test
g.save()
h = HeartRate(user = user1, datetime = rounded_time-timedelta(days=18), ECG = 200) #Month test
h.save()
i = HeartRate(user = user1, datetime = rounded_time-timedelta(weeks=40), ECG = 10) #Year test
i.save()
print(HeartRate.objects.all())

SECONDS_IN_A_YEAR = 31536000
SECONDS_IN_A_MONTH = 2628000
SECONDS_IN_A_WEEK = 604800
SECONDS_IN_A_DAY = 86400
SECONDS_IN_AN_HOUR = 3600

#Temperature - Dense, yearlong test cases. Trend downward
for i in range(5000):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_A_YEAR))
    randomTemp = np.random.uniform(90-i/2000, 100)
    t = Temperature(user = user1, datetime = randomTime , temperature = randomTemp)
    t.save()
print(Temperature.objects.all())

#Accelerometer - Dense, single-day tests. Trend upwards.
for i in range(100):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_A_DAY))
    randomAcc = np.random.uniform(0, 1-(100-i)/200)
    t = Accelerometer(user = user1, datetime = randomTime , x = randomAcc, y = 0, z = 0)
    t.save()
# aa = Accelerometer(user = user1, datetime = rounded_time-timedelta(days=5), x = .5) #Week test
# aa.save()
# ab = Accelerometer(user = user1, datetime = rounded_time-timedelta(days=10), x = .1) #Month test
# ab.save()
# ac = Accelerometer(user = user1, datetime = rounded_time-timedelta(weeks=48), x = 1) #Year test
# ac.save()
print(Temperature.objects.all())

#Gyroscope - Spread out across time scales, kinda logarithmically.
for i in range(100):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_AN_HOUR))
    randomRot = np.random.uniform(0, 1-(100-i)/200)
    t = Gyroscope(user = user1, datetime = randomTime , x = randomRot, y = 0, z = 0)
    t.save()
for i in range(100):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_A_DAY))
    randomRot = np.random.uniform(0, 1-(100-i)/200)
    t = Gyroscope(user = user1, datetime = randomTime , x = randomRot, y = 0, z = 0)
    t.save()
for i in range(100):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_A_WEEK))
    randomRot = np.random.uniform(0, 1-(100-i)/200)
    t = Gyroscope(user = user1, datetime = randomTime , x = randomRot, y = 0, z = 0)
    t.save()
for i in range(100):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_A_MONTH))
    randomRot = np.random.uniform(0, 1-(100-i)/200)
    t = Gyroscope(user = user1, datetime = randomTime , x = randomRot, y = 0, z = 0)
    t.save()
for i in range(100):
    randomTime = rounded_time-timedelta(seconds=random.randrange(SECONDS_IN_A_YEAR))
    randomRot = np.random.uniform(0, 1-(100-i)/200)
    t = Gyroscope(user = user1, datetime = randomTime , x = randomRot, y = 0, z = 0)
    t.save()

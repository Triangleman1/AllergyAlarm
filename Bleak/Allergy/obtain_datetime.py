import datetime

time = datetime.datetime.now()
rounded_time = time - datetime.timedelta(microseconds=time.microsecond)
print(rounded_time)
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    #Comment out to not have to deal with logging in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "allergy_alarm_app/allergy_home.html")

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "allergy_alarm_app/base.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "allergy_alarm_app/login.html", {
                "message": "Invalid credentials"
            })
    return render(request, "allergy_alarm_app/login.html")

def logout_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    logout(request)
    return render(request, "allergy_alarm_app/login.html", {
        "message": "Logged out."
    })

def chart_view(request, sensorType, timeRange):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, 'allergy_alarm_app/chart.html', {
                "sensorType": sensorType,
                "timeRange": timeRange,
            })

def chart_data(request, sensorType, timeRange):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    #Called by chart.html, gives it the proper data. sensorType and timeRange are strings specified by buttons upon clicking.
    present = datetime.now()

    #To edit time-specific plotting settings, change values inside this dictionary
    timeDict ={
        "hour":     {"TimeRange": timedelta(hours=1),
                     "xTimeScale": "minute",
                     },
        "day":      {"TimeRange": timedelta(days=1),
                     "xTimeScale": "hour",
                     },
        "week":     {"TimeRange": timedelta(weeks=1),
                     "xTimeScale": "day",
                     },
        "month":    {"TimeRange": timedelta(weeks=4),
                     "xTimeScale": "day",
                     },
        "year":     {"TimeRange": timedelta(weeks=52),
                     "xTimeScale": "month",
                     },
    }

    #To edit sensor-specific plotting settings, change values inside this dictionary
    sensorDict ={
        "Temperature":      {"table": Temperature, 
                             "plotColumn": "temperature",
                             "fillColor": 'rgb(227, 113, 37, 0.2)',
                             "lineColor": 'rgb(227, 113, 37, 1)',
                             },
        "Heart Rate":       {"table": HeartRate, 
                             "plotColumn": "ECG",
                             "fillColor": 'rgb(213, 18, 18, 0.2)',
                             "lineColor": 'rgb(213, 18, 18, 1)',
                             },
        "Accelerometer":    {"table": Accelerometer, 
                             "plotColumn": "x",
                             "fillColor": 'rgba(75, 192, 192, 0.2)',
                             "lineColor": 'rgba(75, 192, 192, 1)',
                             },
        "Gyroscope":        {"table": Gyroscope, 
                             "plotColumn": "x",
                             "fillColor": 'rgb(113, 14, 193, 0.2)',
                             "lineColor": 'rgb(113, 14, 193, 1)',
                             },
    }

    #This code is time-agnostic and sensor-agnostic - Converts above data into the forms that javascript needs
    timeData = timeDict[timeRange]
    start = present-timeData["TimeRange"]
    xTimeScale = timeData["xTimeScale"]

    sensorData = sensorDict[sensorType]
    data = sensorData["table"].objects.filter(datetime__gte=start).filter(user=request.user).order_by('datetime') #__gte= is syntax for greater than or equal to for django table queries
    values = [[point.datetime, getattr(point, sensorData["plotColumn"])] for point in data] #getattr() takes in a column's name and returns that column
    fillColor = sensorData["fillColor"]
    lineColor = sensorData["lineColor"]

    #print(request.user.username)
    #print(sensorData["table"].user.username)

    #Outputs to chart.html's javascript plotting function
    return JsonResponse(data={
        'values': values,
        'ylabel': sensorType,
        'fillColor': fillColor,
        'lineColor': lineColor,
        'xTimeScale': xTimeScale,
    })
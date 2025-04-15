from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from allergy_alarm_app import templates
import openpyxl
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from .models import *

# Create your views here.
def home(request):
    #Commented out for now so we don't have to deal with logging in
    #if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login"))
    return render(request, "allergy_alarm_app/allergy_home.html")

def dashboard(request):
    #if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login"))
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
    logout(request)
    return render(request, "allergy_alarm_app/login.html", {
        "message": "Logged out."
    })

def chart_view(request, sensorType):
    return render(request, 'allergy_alarm_app/chart.html', {
                "sensorType": sensorType
            })

def chart_data(request, sensorType):
    #Called by chart.html, gives it the proper data. sensorType is a string which should match the sensor and table name
    if (sensorType == "Temperature"): 
        print("test:temp")
        data = Temperature.objects.all()
        values = [point.temperature for point in data]
    elif (sensorType == "HeartRate"): 
        data = HeartRate.objects.all()
        values = [point.ECG for point in data]
    elif (sensorType == "Accelerometer"): 
        print("test:accel")
        data = Accelerometer.objects.all()
        values = [point.x for point in data]
    elif (sensorType == "Gyroscope"): 
        data = Gyroscope.objects.all()
        values = [point.x for point in data]
    print([point.userID for point in data])
    labels = [point.datetime.strftime("%B %d, %I:%M%p") for point in data] #if point.user_id == user
    return JsonResponse(data={
        'labels': labels,
        'values': values,
        'ylabel': sensorType,
    })


# def excel_to_chart(request):
#     # Your Excel file path (or it could be uploaded by the user in a form)
#     excel_file_path = 'TestFile.xlsx'

#     # Read the Excel file using openpyxl
#     workbook = openpyxl.load_workbook(excel_file_path)
#     sheet = workbook.active

#     # Extract data from the Excel sheet (assumes data starts from row 2)
#     # For example, assume the Excel sheet has columns 'Date' and 'Value'
#     dates = []
#     values = []

#     for row in sheet.iter_rows(min_row=2, values_only=True):
#         dates.append(row[0])  # assuming 'Date' is the first column
#         values.append(row[1])  # assuming 'Value' is the second column

#     # Create a chart using matplotlib
#     fig, ax = plt.subplots()
#     ax.plot(dates, values, marker='o', linestyle='-', color='b')

#     ax.set(xlabel='Date', ylabel='Value',
#            title='Example Data Visualization')

#     # Generate the plot and send as response
#     response = HttpResponse(content_type='image/png')
#     canvas = FigureCanvas(fig)
#     canvas.print_png(response)
#     return response

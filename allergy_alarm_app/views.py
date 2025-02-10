from django.shortcuts import render
from django.http import HttpResponse
from allergy_alarm_app import templates

# Create your views here.
def home(request):
    return render(request, "allergy_alarm_app/allergy_home.html")

def dashboard(request):
    return render(request, "allergy_alarm_app/base.html")
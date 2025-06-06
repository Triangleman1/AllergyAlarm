"""
URL configuration for allergy_alarm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from allergy_alarm_app import views

app_name = "allergy"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    #path("chart", views.excel_to_chart, name='excel_chart'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('chart/<str:sensorType>/<str:timeRange>', views.chart_view, name='chart'),
    path('chart-data/<str:sensorType>/<str:timeRange>', views.chart_data, name='chart-data'),
]

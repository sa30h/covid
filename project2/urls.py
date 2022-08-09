"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard),
    path('insetdata/', views.get_data),
    path('getallapi/', views.CR_CovidApiView.as_view()),
    path('getbyid/<id>', views.U_CovidApiView.as_view()),
    path('getbycountry/<country>', views.Getbycountry.as_view()),
    path('getbydate/<date>', views.Getbydate_ExchangeApiView.as_view()),
]

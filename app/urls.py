from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [

    path('', views.index, name='index'),
    path('thanks', views.thanks, name='thanks'),
    path('submitForm', views.submitForm, name='submitForm'),
    path('test',views.getGroup)
        
]

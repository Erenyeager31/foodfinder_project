from django.contrib import admin
from django.urls import path,include
from foodfinder_app import views

urlpatterns = [
    path('',views.index,name='home'),
]

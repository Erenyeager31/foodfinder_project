from django.contrib import admin
from django.urls import path,include
from foodfinder_app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.index,name='home'),
    path('create_account',views.create_act,name='create_act'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('signup_processing',views.signup_processing,name='signup'),
    path('login_processing',views.login_processing,name='login_processing'),
]


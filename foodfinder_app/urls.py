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
    path('profile',views.profile,name='view_profile'),
    path('logout',views.logout,name='logout'),
    path('fill_details_seller',views.s_fill_details,name='s_fill_details'),
    path('s_save_details',views.s_save_details,name='s_save_details'),
    path('uploadfood',views.uploadfood,name='uploadfood'),
]


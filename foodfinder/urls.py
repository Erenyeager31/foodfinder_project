"""
URL configuration for foodfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('foodfinder_app.urls')),
    path('home',include('foodfinder_app.urls')),
    path('create_account',include('foodfinder_app.urls')),
    path('sign_in',include('foodfinder_app.urls')),
    path('aboutus',include('foodfinder_app.urls')),
    path('contactus',include('foodfinder_app.urls')),
    path('signup_processing',include('foodfinder_app.urls')),
    path('login_processing',include('foodfinder_app.urls')),
    path('profile',include('foodfinder_app.urls')),
    path('logout',include('foodfinder_app.urls')),
    path('fill_details_seller',include('foodfinder_app.urls')),
    path('s_save_details',include('foodfinder_app.urls')),
    path('uploadfood',include('foodfinder_app.urls')),
    path('food_upload_form',include('foodfinder_app.urls')),
    path('checkorder',include('foodfinder_app.urls')),
    path('AddtoCart',include('foodfinder_app.urls')),
    path('save_location',include('foodfinder_app.urls')),
    path('showmaps',include('foodfinder_app.urls')),
    path('showcart',include('foodfinder_app.urls')),
    path('delete_cart',include('foodfinder_app.urls')),
    path('checkout',include('foodfinder_app.urls')),
    path('fetch_location',include('foodfinder_app.urls')),
    path('search_filter',include('foodfinder_app.urls')),
    path('listShop',include('foodfinder_app.urls')),
    path('review_page',include('foodfinder_app.urls')),
    path('submit_review',include('foodfinder_app.urls')),
    path('shop_review',include('foodfinder_app.urls')),
]

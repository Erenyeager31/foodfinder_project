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
    path('food_upload_form',views.food_upload_form,name='food_upload_form'),
    path('checkorder',views.check_orders,name='checkorder'),
    path('AddtoCart',views.add_to_cart,name='AddtoCart'),
    path('save_location',views.save_location,name='save_location'),
    path('showmaps',views.showmaps,name='showmaps'),
    path('showcart',views.showcart,name='showcart'),
    path('delete_cart',views.delete_cart,name='delete_cart'),
    path(r'view_item/',views.view_item,name='view_item'),
    path('fetch_location',views.fetch_location,name='fetch_location'),
    path('search_filter',views.search_filter,name='search_filter'),
    path('listShop',views.listShop,name='listShop'),
    path('review_page',views.review_page,name='review_page'),
    path('submit_review',views.submit_review,name='submit_review'),
    path('shop_review',views.shop_reviews,name='shop_review'),
    path('checkout',views.checkout,name='checkout'),
    path(r'buyitem/',views.buyitem,name='buyitem'),
    # path('predict',views.predict,name='predict'),
    path('place_order',views.place_order,name='place_order'),
]


from django.contrib import admin
from foodfinder_app.models import seller_details,user_detail,food_detail

# Register your models here.
admin.site.register(seller_details)
admin.site.register(user_detail)
admin.site.register(food_detail)

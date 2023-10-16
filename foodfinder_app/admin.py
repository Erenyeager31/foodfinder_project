from django.contrib import admin
from foodfinder_app.models import seller_details,user_detail,food_detail,cart,business_location,review,shop_review,order_history,order_list


# Register your models here.
admin.site.register(seller_details)
admin.site.register(user_detail)
admin.site.register(food_detail)
admin.site.register(cart)
admin.site.register(business_location)
admin.site.register(review)
admin.site.register(shop_review)
admin.site.register(order_history)
admin.site.register(order_list)
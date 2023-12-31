from django.db import models

# Create your models here.
class seller_details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=12)
    role = models.CharField(max_length=15)
    business_name = models.CharField(max_length=20,default="")
    bank_act_no = models.CharField(max_length=11,default="")
    ifsc = models.CharField(max_length=17,default="")
    branch_name = models.CharField(max_length=15,default="")
    city = models.CharField(max_length=15,default="")
    state = models.CharField(max_length=15,default="")
    zip = models.CharField(max_length=6,default="")
    shop_add = models.CharField(max_length=100,default="")
    location = models.CharField(max_length=30,default="")
    avg_ratings = models.IntegerField(default=1)
    def __str__(self):
        return self.name + str(self.id) + "" + self.business_name
    
class user_detail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=12)
    role = models.CharField(max_length=15)
    city = models.CharField(max_length=15,default='')
    state = models.CharField(max_length=15,default='')
    zip = models.CharField(max_length=15,default='')
    address = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.name + str(self.id)
    
class food_detail(models.Model):
    username = models.CharField(max_length=10)
    food_name = models.CharField(max_length=25)
    food_cat = models.CharField(max_length=15)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    img_url = models.CharField(max_length=100)
    avg_ratings = models.IntegerField(default=0)
    def __str__(self):
        return self.food_name + str(self.id)

class cart(models.Model):
    username = models.CharField(max_length=10)
    food_id = models.IntegerField()
    def __str__(self):
        return self.username+" "+str(self.food_id)
    
class business_location(models.Model):
    username = models.CharField(max_length=10)
    business_name = models.CharField(max_length=20,default="")
    location = models.CharField(max_length=30,default="")
    def __str__(self):
        return self.business_name + self.username

class review(models.Model):
    food_id = models.IntegerField()
    rating = models.CharField(max_length=10)
    review = models.CharField(max_length=100)
    username = models.CharField(max_length=10)
    def __str__(self):
        return self.username+" "+str(self.food_id)
    
class shop_review(models.Model):
    # business_name = models.CharField(max_length=30)
    business_id = models.IntegerField(default=0)
    rating = models.CharField(max_length=10)
    review = models.CharField(max_length=100)
    username = models.CharField(max_length=10)
    def __str__(self):
        return self.username+" "+ str(self.business_id)
    
class order_history(models.Model):
    username = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    food_ids = models.CharField(max_length=100,default="")
    total_price = models.IntegerField()
    def __str__(self):
        return self.username+" "+str(self.timestamp)
    
class order_list(models.Model):
    s_username = models.CharField(max_length=10)
    food_id = models.IntegerField()
    username = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.s_username+" "+self.username
    


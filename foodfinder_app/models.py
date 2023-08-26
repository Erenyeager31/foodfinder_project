from django.db import models

# Create your models here.
class seller_details(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=12)
    role = models.CharField(max_length=15)
    shop_name = models.CharField(max_length=20,default="")
    shop_add = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name
    
class user_detail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=12)
    role = models.CharField(max_length=15)
    def __str__(self):
        return self.name
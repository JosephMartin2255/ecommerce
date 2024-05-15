from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.category_name
class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=255,null=True)
    product_description=models.CharField(max_length=255,null=True)
    product_price=models.IntegerField(null=True)
    product_image=models.ImageField(upload_to="image/",null=True)
    def __str__(self):
        return self.product_name
class userdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,null=True)
    number=models.CharField(max_length=255,null=True)
    img=models.ImageField(upload_to="image/",null=True)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prod=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1)
    def total_price(self):
        return self.quantity*self.prod.product_price

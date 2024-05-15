from django.contrib import admin
from eapp.models import Category
from eapp.models import Products
from eapp.models import userdetails
# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(userdetails)
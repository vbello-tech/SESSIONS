from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display=['name', 'category', 'city', 'active',]
    list_filter=['name','code',]

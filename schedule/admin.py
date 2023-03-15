from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BookedSession)
class BookedSessionAdmin(admin.ModelAdmin):
    list_display=['user', 'business', 'active',]
    list_filter=['business',]


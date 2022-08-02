from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(booking)
class admin_teacher(admin.ModelAdmin):
    list_display =['name','created_at_data','select_class']
    pass


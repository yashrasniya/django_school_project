from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Teachers)
class admin_teacher(admin.ModelAdmin):
    pass


@admin.register(classes)
class admin_classes(admin.ModelAdmin):
    pass


@admin.register(blog)
class admin_blog(admin.ModelAdmin):
    pass


@admin.register(images)
class admin_images(admin.ModelAdmin):
    pass


@admin.register(school_basic_detail)
class admin_school_basic_detail(admin.ModelAdmin):
    pass

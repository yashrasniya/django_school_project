from django.contrib import admin
from .models import Document


# Register your models here.
@admin.register(Document)
class documentAdmin(admin.ModelAdmin):
    list_display = ['title', 'File']
    # change_list_template = "document/button.html"

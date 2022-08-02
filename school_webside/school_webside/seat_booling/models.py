from django.db import models


# Create your models here.

class booking(models.Model):
    name = models.CharField(max_length=32, null=False)
    Phone = models.CharField(max_length=12, null=False)
    email = models.EmailField(blank=True, null=True)
    select_class = models.CharField(max_length=12, blank=True, null=True)
    created_at_time = models.TimeField(auto_created=True,null=True)
    created_at_data = models.DateField(auto_created=True,null=True)

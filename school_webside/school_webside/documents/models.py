from django.db import models


# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=300, blank=True)
    File = models.FileField(upload_to='document', blank=True)

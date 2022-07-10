from django.db import models


# Create your models here.

class Teachers(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    teaching_subject = models.CharField(max_length=60, blank=False, null=False)
    Social_media_id = models.URLField(blank=True)
    img = models.ImageField()
    Experience = models.IntegerField(blank=True)


class classes(models.Model):
    class_name = models.CharField(max_length=60, blank=False, null=False)
    class_description = models.TextField(max_length=256, blank=False, null=False)
    class_times = models.CharField(max_length=60, blank=False, null=False)
    fee = models.IntegerField( blank=False, null=False)
    class_img = models.ImageField(blank=True)


class blog(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    detail = models.TextField(max_length=30, blank=False, null=False)
    blog_img = models.ImageField(blank=True)
    file = models.FileField(blank=True)


class images(models.Model):
    images = models.ImageField(upload_to='img/upload')


class school_basic_detail(models.Model):
    about_school = models.TextField(max_length=500, blank=False, null=False)
    address = models.CharField(max_length=60, blank=False, null=False)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12, blank=False, null=False)
    Facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

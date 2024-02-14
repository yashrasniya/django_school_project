from django.db import models


# Create your models here.

class Teachers(models.Model):
    name = models.CharField(max_length=600, blank=False, null=False)
    teaching_subject = models.CharField(max_length=600, blank=False, null=False)
    Social_media_id = models.URLField(blank=True)
    img = models.ImageField()
    Experience = models.IntegerField(blank=True)


class classes(models.Model):
    class_name = models.CharField(max_length=600, blank=False, null=False)
    class_description = models.TextField(max_length=2560, blank=False, null=False)
    class_times = models.CharField(max_length=60, blank=False, null=False)
    fee = models.IntegerField(blank=False, null=False)
    class_img = models.ImageField(blank=True)


class blog(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    detail = models.TextField(max_length=3000, blank=False, null=False)
    blog_img = models.ImageField(blank=True)
    link=models.URLField(blank=True)
    file = models.FileField(blank=True)


class images(models.Model):
    images = models.ImageField(upload_to='img/upload')


class school_basic_detail(models.Model):
    about_school = models.TextField(max_length=500, blank=False, null=False)
    contact_description = models.TextField(max_length=500, blank=False, null=False)
    opening_Hours = models.TextField(max_length=500, blank=False, null=False)
    address = models.CharField(max_length=600, blank=False, null=False)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12, blank=False, null=False)
    Facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


class Facilities(models.Model):
    Facilities_title = models.CharField(max_length=32, blank=False, null=False)
    Facilities_description = models.TextField(max_length=300, blank=False, null=False)
    Facilities_icon = models.CharField(max_length=32, blank=True, null=True)


class About_school(models.Model):
    title = models.CharField(max_length=320, blank=False, null=False)
    about_detail = models.TextField(max_length=3200, blank=False, null=False)
    about_img1 = models.ImageField(upload_to='img/upload')
    about_img2 = models.ImageField(upload_to='img/upload')
    points_1 = models.CharField(max_length=32, blank=True, null=True)
    points_2 = models.CharField(max_length=32, blank=True, null=True)
    points_3 = models.CharField(max_length=32, blank=True, null=True)


class MainHeading(models.Model):
    title = models.CharField(max_length=320, blank=False, null=False)
    about = models.TextField(max_length=3000, blank=False, null=False)
    images = models.ImageField(upload_to='img/upload')
    school_logo = models.ImageField(upload_to='img/upload')


class testimonial(models.Model):
    person_name = models.CharField(max_length=32, blank=False, null=False)
    person_profession = models.CharField(max_length=32, blank=False, null=False)
    person_img = models.ImageField(upload_to='img/upload',blank=True)
    testimonial_data = models.TextField(max_length=300, blank=False, null=False)
    testimonial_verified = models.BooleanField( blank=False, null=False)

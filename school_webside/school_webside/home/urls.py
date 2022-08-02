from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home_page),
    path('Teachers', teacher_page),
    path('classes', classes_page),
    path('about', about_page),
    path('gallery', gallery_page),
    path('contact', contact_page),

]

from django.urls import include, path
from .views import *

urlpatterns = [

    path('booking', booking_view),

]

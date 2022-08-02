from django.shortcuts import render
from django.http import *
from .models import *
import datetime


# Create your views here.

def booking_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        class_name = request.POST['class_name']
        obj = booking.objects.create(name=name, Phone=phone, email=email,
                                     select_class=class_name,
                                     created_at_data=datetime.datetime.now().date().__str__(),
                                     created_at_time=datetime.datetime.now().time().__str__()
)
        obj.save()
        return HttpResponseRedirect('/')
    elif request.method == 'GET':
        return HttpResponse({'error':404})
    else:
        return Http404('only post requests !!!!!')

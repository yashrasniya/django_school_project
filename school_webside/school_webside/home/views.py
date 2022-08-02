from django.shortcuts import render
from django.http import *
from .models import *


# Create your views here.
def all_data():
    teachers = Teachers.objects.all()
    f = Facilities.objects.all()
    c = classes.objects.all()
    b = blog.objects.all()
    de = school_basic_detail.objects.all()
    about = About_school.objects.all()
    main_heading = MainHeading.objects.all()
    img = images.objects.all()
    school_logo=main_heading[:1:-1][0].school_logo
    data = {'school_name': 'SGSVMIC',
            'teachers': teachers[:4],
            'Facilities': f[:6],
            'classes': c[:3],
            'blog': b[:3:-1],
            'school_detail': de[:1:-1],
            'about': about[:1:-1],
            'main_heading': main_heading[:1:-1],
            'images': img,
            'school_logo':school_logo}
    return data


def home_page(request):
    return render(request, 'html/pages/home.html', all_data()
                  )


def teacher_page(request):
    return render(request, 'html/pages/teachers.html', all_data())


def classes_page(request):
    return render(request, 'html/pages/class.html', all_data())


def about_page(request):
    return render(request, 'html/pages/about.html', all_data())


def gallery_page(request):
    return render(request, 'html/pages/Gallery.html', all_data())


def contact_page(request):
    return render(request, 'html/pages/contact.html', all_data())

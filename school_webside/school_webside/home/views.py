from django.shortcuts import render
from django.http import *
from django.conf import settings
from .models import *
from documents.models import *


# Create your views here.
def all_data():
    media_url = settings.MEDIA_URL
    teachers = Teachers.objects.all()
    f = Facilities.objects.all()
    tes = testimonial.objects.all()
    c = classes.objects.all()
    b = blog.objects.all()
    de = school_basic_detail.objects.all()
    about = About_school.objects.all()
    main_heading = MainHeading.objects.all()
    img = images.objects.all()
    school_logo = main_heading[:1:-1][0].school_logo
    documents=Document.objects.filter(show=True)
    data = {'school_name': 'SGSVMIC',
            'teachers': teachers[:4:-1],
            'Facilities': f[:6],
            'classes': c[:3],
            'blog': b[:3:-1],
            'school_detail': de[:1:-1],
            'about': about[:1:-1],
            'main_heading': main_heading[:1:-1],
            'images': img,
            'school_logo': school_logo,
            'media_url': media_url,
            'testimonial': tes[:10:-1],
            'documents':documents}
    return data


def home_page(request):
    return render(request, 'html/pages/home.html', all_data()
                  )


def teacher_page(request):
    teachers = Teachers.objects.all()
    data = all_data()
    data['teachers'] = teachers[::-1]
    return render(request, 'html/pages/teachers.html', data)


def classes_page(request):
    c = classes.objects.all()
    data = all_data()
    data['classes'] = c[::-1]
    return render(request, 'html/pages/class.html', data)


def about_page(request):
    return render(request, 'html/pages/about.html', all_data())


def gallery_page(request):
    return render(request, 'html/pages/Gallery.html', all_data())


def contact_page(request):
    return render(request, 'html/pages/contact.html', all_data())


def testimonial_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        testimonial_data = request.POST['testimonial_data']
        profession = request.POST['profession']

        tes = testimonial.objects.create(person_name=name,
                                         person_profession=profession,
                                         testimonial_data=testimonial_data,
                                         testimonial_verified=True
                                         )
        tes.save()
        data = all_data()
        data['Done'] = True
        return render(request, 'html/pages/testimonial.html', data)
    else:

        return render(request, 'html/pages/testimonial.html', all_data())


def blogs_page(request):
    c = blog.objects.all()
    data = all_data()
    data['blog'] = c[::-1]
    return render(request, 'html/pages/blog.html', data)

def public_disclosure(request):
    return render(request, 'html/pages/public_disclosure.html', all_data()
                  )
from django.shortcuts import render
from .models import Course
# Create your views here.
def course_list(request):
    # courses = courses.objects.all()
    courses = Course._default_manager.all()
    return render(request,"courseapp/course_list.html",{"Courses":courses})
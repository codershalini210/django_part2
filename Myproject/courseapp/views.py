from django.shortcuts import get_object_or_404, render
from .models import Course
# Create your views here.
def course_list(request):
    # courses = courses.objects.all()
    courses = Course._default_manager.all()
    return render(request,"courseapp/course_list.html",{"Courses":courses})

def course_detail(request,pk):
    course = get_object_or_404(Course,pk=pk)
    return render(request,"courseapp/coursedetails.html",{"course":course})
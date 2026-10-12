
from django.views.generic import ListView,DetailView
from .models import Course
class CourseListView(ListView):
    model = Course
    template_name="courseapp/course_list.html"
    context_object_name = "Courses"
class CourseDetailView(DetailView):
    model=Course
    template_name="courseapp/coursedetails.html"
    context_object_name = "course"
# from django.shortcuts import get_object_or_404, render
# from .models import Course

# def course_list(request):

#     courses = Course._default_manager.all()
#     return render(request,"courseapp/course_list.html",{"Courses":courses})

# def course_detail(request,pk):
#     course = get_object_or_404(Course,pk=pk)
#     return render(request,"courseapp/coursedetails.html",{"course":course})
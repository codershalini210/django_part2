from django.contrib import admin
# from . import models
from .models import Course
# Register your models here.
admin.site.register(Course)
# admin.site.register(models.Course)
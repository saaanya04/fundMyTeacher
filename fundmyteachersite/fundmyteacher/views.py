from django.shortcuts import render
from django.http import HttpResponse
from .models import TeacherInfo
from .models import SchoolInfo

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="fundmyteacher/home.html",
                  context={"teacherinfo": TeacherInfo.objects.all})
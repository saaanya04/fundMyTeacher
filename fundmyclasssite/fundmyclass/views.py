from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TeacherInfo
from .models import SchoolInfo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.exceptions import *
from .forms import NameForm
from .forms import TeacherForm



# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="fundmyclass/home.html",
                  context={"teacherinfo": TeacherInfo.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("fundmyclass:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")


    form = NewUserForm
    return render(request,
                   "fundmyclass/register.html",
                   context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("fundmyclass:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("fundmyclass:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                  "fundmyclass/login.html",
                  {"form":form})

""" class SearchResultsView(ListView):
    model = TeacherInfo
    template_name = 'search.html' """


def search(request):
        # if this is a POST request we to process form data
    print(request)
    if request.method == 'GET':
        # create a form instance and populate it with data from the request
        form = NameForm(request.GET)
        print('testGet1')
        #form = NameForm
        print('testGet2')
        if form.is_valid():
            query = request.GET.get('first_name')
            print(query)
            if query:
                #qset = TeacherInfo.objects.filter(first_name__icontains=query)
                #qset = (
                    #Q(first_name__icontains=query)
                #)
                #bbh = TeacherInfo.objects.filter(qset)
                #bby = TeacherInfo.objects.filter(first_name__icontains=query)
                print('candy')
                return render(request, 'fundmyclass/search.html', {'teacherinfo': TeacherInfo.objects.filter(first_name__icontains=query)})
                #return bbh
            #else:
                #return TeacherInfo.objects.all()
                #qset = []
                #return render(request, "fundmyclass/search.html", { "query": query})
            # check whether it's valid
                #if form.is_valid():
                    #print('VALID')
                #else:
                    #print('not_valid')
                    #first_name = form.cleaned_data.get('q')
                    #query = self.request.GET.get('q')
                    #object_list = TeacherInfo.objects.filter(
                        #Q(first_name__icontains=first_name))
                    #return object_list
                    # name = authenticate(first_name=first_name)
                    #if first_name is not None:
                        # redirect to a new URL:
                    #return redirect("fundmyclass:results")
                    #return HttpResponseRedirect('/search/')

    else:
        form = NameForm(request.POST)
        if form.is_valid():
            print('VALIDPost')
        first_name = form.cleaned_data.get('q')

    return render(request, 'fundmyclass/search.html', {'form': form})


def registerTeacher(request):
    # if this is a POST request we to process form data
    print(request)
    if request.method == 'GET':
        # create a form instance and populate it with data from the request
        print('testGet1')
        form = TeacherForm

    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            print('VALIDPost')
        myTeach = TeacherInfo()
        myTeach = form.save()

    return render(request, 'fundmyclass/registerTeacher.html', {'form': form})


"""def results(request):
     return render(request,
                "fundmyclass/results.html",
                context={"teacherinfo":TeacherInfo.objects.first_name})"""



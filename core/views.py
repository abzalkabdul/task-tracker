from operator import ge
import re
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Task, Taskgroup, Project

from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    form = CreateUserForm() # for GET request

    if request.method == 'POST':
        action = request.POST.get("action")
        if action == 'register':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account {user} is created!')
                return redirect('login')
    return render(request, 'registration.html', {'form': form})


def login_page(request):
    form = AuthenticationForm()

    if request.method=='POST' and request.POST.get('action') == 'login':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:main')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html', {'form': form})

def logout_page(request):
    if request.method == 'POST' and request.POST.get("action") == 'logout':
        logout(request)
        return redirect('core:base')

def base(request):
    return render(request, 'base.html', {"first_project": get_first_project_name})

def main(request):
    projects = Project.objects.all()
    return render(request, 'main.html', {"first_project": get_first_project_name, 
                                         "projects": projects})


def get_first_project_name():
    if Project.objects.all():
        return Taskgroup.objects.first().project.name
    return "Project"

def specified_project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'specified_project.html', {"first_project": get_first_project_name,
                                                      "project": project})




from django.shortcuts import render
from django.shortcuts import redirect

from .models import Task, Taskgroup

from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    form = CreateUserForm() # for GET request

    if request.method == 'POST':
        action = request.POST.get("action")
        if  action == 'register':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account {user} is created!')
                return redirect('login')
    return render(request, 'registration.html', {'form': form})


def login_page(request):
    form = AuthenticationForm()

    if request.POST.get('action') == 'login':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:base')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html', {'form': form})

def logout_page(request):
    if request.POST.get("action") == 'logout':
        logout(request)
        return redirect('core')


def base(request):
    tasks = Task.objects.all()
    first_project = Taskgroup.objects.first().project_name
    return render(request, 'base.html', {"tasks": tasks,
                                         "first_project": first_project,})



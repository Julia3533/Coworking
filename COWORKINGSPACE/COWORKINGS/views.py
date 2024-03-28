from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User, Project, Task


def index(request):
    return render(request, "index.html", {
        "projects":Project.objects.all()
    
    })

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "login.html", {
            })
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

def create_project(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        project = Project(name=name, description=description)

        project.save()

        return render(request, 'create_project.html')
    else:
        return render(request, 'create_project.html')

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks})


def add_task(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']

        task = Task(name=name, description=description, project=project)
        task.save()

        return HttpResponseRedirect(reverse('project_detail', args=(project.id,)))
    else:
        return render(request, 'add_task.html', {'project': project})

def edit_task(request, project_id, task_id):
    task = Task.objects.get(id=task_id)
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.save()
        return HttpResponseRedirect(reverse('project_detail', args=(project.id,)))
    else:
        return render(request, 'edit_task.html', {'task': task})

def delete_task(request, project_id, task_id):
    task = Task.objects.get(id=task_id)
    project_id = task.project.id
    project = Project.object.get(id=project_id)
    task.delete()
    return HttpResponseRedirect(reverse('project_detail', args=(project.id,)))





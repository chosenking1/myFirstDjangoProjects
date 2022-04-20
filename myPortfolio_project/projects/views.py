from pydoc import describe
from tkinter.tix import Form
from django.shortcuts import render
from .forms import ProjectForm
from .models import Project


def create_project(request):
    data = request.POST
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(data=data)
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            form = ProjectForm()
        else:
            print("This object will not save!")
            print("The technology should not be person.")
            print(form.errors)
    return render(request, "projects/create_project.html", {"form": form})


def get_projects(request):
    projects = Project.objects.all().order_by('-date_created')
    return render(request, "projects/project_list.html", {"projects": projects})


def filter_projects(request):
    data = request.POST
    key = data.get('filter')
    projects = {} if key is None else Project.objects.filter(title__contains=key)
    return render(request, "projects/filtered_projects.html", {'projects': projects})

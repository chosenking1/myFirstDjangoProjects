from django.shortcuts import render
from django.http import request

from .forms import ProjectForm
from projects.models import Project


# Create your views here.
def create_projects(request):
    form = ProjectForm()
    print(request, "====")
    print(form)
    data = request.POST
    print(data, "===data===")
    if request.method == "POST":
        form = ProjectForm(data=data)
        # form.save
        # if form.is_valid():
        #     form.save()
        #     form = ProjectForm()
        #
        # else:
        #     print(form.errors)
    return render(request, 'projects/create_project.html', {"form": form})


def get_projects(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})

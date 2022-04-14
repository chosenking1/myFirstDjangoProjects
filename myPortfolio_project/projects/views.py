from django.shortcuts import render
from django.http import request
from .forms import ProjectForm


# Create your views here.
def create_projects(request):
    forms = ProjectForm()
    print(request, "====")
    print(forms)
    data = request.POST
    print(data, "===data===")
    if request.method == "POST":
        form = ProjectForm(data=data)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'projects/create_project.html', {"form": forms})

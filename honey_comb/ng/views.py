from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path


# Create your views here.
def ng_login(request):
    return render(request, "login.html", context={"country": "Nigeria"})


def ng_register(request):
    return render(request, "register.html", context={"country": "Nigeria"})

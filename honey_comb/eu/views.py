from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path


def eu_login(request):
    return render(request, "login.html", context={"country": "Europeans"})


def eu_register(request):
    return render(request, "register.html", context={"country": "Europeans"})

# Create your views here.

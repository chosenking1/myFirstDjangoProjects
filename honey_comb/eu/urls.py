from django.http import HttpResponse
from django.urls import path

from eu import views


urlpatterns = [
    path('login/', views.eu_login),
    path('register/', views.eu_register),
]

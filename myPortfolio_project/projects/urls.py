from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_projects),
    path('get/', views.get_projects)
]

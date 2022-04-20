from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_project),
    path('get/', views.get_projects),
    path('filter/', views.filter_projects),
]
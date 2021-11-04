from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/template/', views.Template.as_view())
]
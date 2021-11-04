from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/<str:ProjectId>', views.Project.as_view()),
]
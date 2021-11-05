from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/<str:ProjectId>', views.Project.as_view()),
    path('project/<str:ProjectId>/book', views.BookList.as_view()),
    path('project/<str:ProjectId>/<str:BookId>', views.Book.as_view()),
    path('project/<str:ProjectId>/<str:BookId>/chapter', views.Chapter.as_view()),
    path('project/<str:ProjectId>/<str:BookId>/<int:ChapterId>', views.Chapter.as_view())
]
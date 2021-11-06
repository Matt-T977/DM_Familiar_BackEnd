from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/<str:ProjectId>', views.Project.as_view()),
    path('project/<str:ProjectId>/book/list', views.BookList.as_view()),
    path('project/<str:ProjectId>/book/<str:BookId>', views.Book.as_view()),
    path('project/<str:ProjectId>/book/<str:BookId>/chapter/list', views.ChapterList.as_view()),
    path('project/<str:ProjectId>/book/<str:BookId>/chapter/<str:ChapterId>', views.Chapter.as_view()),
    path('project/<str:ProjectId>/static/list', views.StaticAssetList.as_view()),
    path('project/<str:ProjectId>/static/<str:StaticAssetId>', views.StaticAsset.as_view()),
    path('project/<str:ProjectId>/video/list', views.VideoList.as_view()),
    path('project/<str:ProjectId>/video/<str:VideoId>', views.Video.as_view()),
    path('project/<str:ProjectId>/audio/list', views.AudioList.as_view()),
    path('project/<str:ProjectId>/audio/<str:AudioId>', views.Audio.as_view()),
    path('project/<str:ProjectId>/location/list', views.LocationList.as_view()),
    path('project/<str:ProjectId>/location/<str:LocationId>', views.Location.as_view()),
    path('project/<str:ProjectId>/location/<str:LocationId>/minor-location/list', views.MinorLocationList.as_view()),
    path('project/<str:ProjectId>/location/<str:LocationId>/minor-location/<str:MinorLocationId>', views.MinorLocation.as_view()),
    path('project/<str:ProjectId>/character/list', views.CharacterList.as_view()),
    path('project/<str:ProjectId>/character/<str:CharacterId>', views.Character.as_view()),
]
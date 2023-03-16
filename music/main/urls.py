from django.urls import path
from .views import AlbumListCreateView,\
    AlbumDetail, SongDetailView, SongListCreateView


urlpatterns = [
    path('albums/', AlbumListCreateView.as_view()),
    path('albums/<int:pk>/', AlbumDetail.as_view()),
    path('songs/', SongListCreateView.as_view()),
    path('songs/<int:pk>/', SongDetailView.as_view()),

]
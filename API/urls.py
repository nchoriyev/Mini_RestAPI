from django.urls import path
from .views import ArtistListAPIView, ArtistDetailAPIView, AlbomListAPIView, AlbomDetailAPIView, SongListAPIView, SongDetailAPIView

urlpatterns = [
    path('artists/', ArtistListAPIView.as_view(), name='artist-list'),
    path('artists/<int:id>/', ArtistDetailAPIView.as_view(), name='artist-detail'),
    path('alboms/', AlbomListAPIView.as_view(), name='albom-list'),
    path('alboms/<int:id>/', AlbomDetailAPIView.as_view(), name='albom-detail'),
    path('songs/', SongListAPIView.as_view(), name='song-list'),
    path('songs/<int:id>/', SongDetailAPIView.as_view(), name='song-detail'),
]

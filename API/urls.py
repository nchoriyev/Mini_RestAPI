from django.urls import path
from .views import ArtistViewSet, AlbomViewSet, SongViewSet

urlpatterns = [
    path('artist/', ArtistViewSet.as_view(), name='artist'),
    path('albom/', AlbomViewSet.as_view(), name='albom'),
    path('song/', SongViewSet.as_view(), name='song'),
]
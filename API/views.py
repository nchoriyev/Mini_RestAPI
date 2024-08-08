from rest_framework import viewsets
from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer
from rest_framework.permissions import IsAuthenticated

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]

class AlbomViewSet(viewsets.ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    permission_classes = [IsAuthenticated]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

class TelegramArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []


from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer


class ArtistViewSet(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)

        return Response(data=serializer.data)


class AlbomViewSet(APIView):
    def get(self, request):
        queryset = Albom.objects.all()
        serializer = AlbomSerializer(queryset, many=True)

        return Response(data=serializer.data)


class SongViewSet(APIView):
    def get(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset, many=True)

        return Response(data=serializer.data)

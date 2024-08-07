from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Artist, Albom, Song
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer


class ArtistListAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if query:
            queryset = Artist.objects.filter(name__icontains=query)
        else:
            queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbomListAPIView(APIView):
    def get_queryset(self):
        return Albom.objects.all()

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(name__icontains=search_data)

        serializer = AlbomSerializer(query, many=True)
        return Response(data=serializer.data)


    def post(self, request):
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbomDetailAPIView(APIView):
    def get(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(albom)
        return Response(serializer.data)

    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=albom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        albom = Albom.objects.get(id=id)
        albom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongListAPIView(APIView):
    def get_queryset(self):
        return Song.objects.all()

    def get(self, request):
        query = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            query = query.filter(name__icontains=search_data)

        serializer = SongSerializer(query, many=True)
        return Response(data=serializer.data)
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = Song.objects.get(id=id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

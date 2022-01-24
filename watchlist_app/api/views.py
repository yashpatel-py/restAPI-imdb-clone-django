from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movies = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movies)
        return Response(serializer.data)

    def put(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        # serializer = StreamPlatformSerializer(platform, many = True, context={'request': request})
        serializer = StreamPlatformSerializer(platform, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            streamPlatform_single_data = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "StreamPlatform not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(streamPlatform_single_data)
        return Response(serializer.data)

    def put(self, request, pk):
        streamplatformss = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(streamplatformss, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        del_stream = StreamPlatform.objects.get(pk=pk)
        del_stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
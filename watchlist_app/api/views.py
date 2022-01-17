from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return Response(serializer.data)

@api_view()
def movie_detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)
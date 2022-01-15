from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse 

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': list(movies.values())
    }
    return JsonResponse(context)
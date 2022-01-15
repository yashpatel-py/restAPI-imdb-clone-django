from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.movie_list, name='movie-list'),
]
from django.urls import path
from watchlist_app.api import views


urlpatterns = [
    path('list/', views.movie_list, name='movie-list'),
    path('<int:pk>', views.movie_detail, name="movie-detail")
]
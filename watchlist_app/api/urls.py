from django.urls import path
from watchlist_app.api import views


urlpatterns = [
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>', views.movie_detail, name="movie-detail")
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name="movie-detail"),
    path('platform/', views.StreamPlatformAV.as_view(), name='platform-list'),
    path('platform/<int:pk>', views.StreamPlatformDetailAV.as_view(), name="platform-detail")
]
from django.urls import path
from watchlist_app.api import views


urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name="movie-detail"),
    path('stream/', views.StreamPlatformAV.as_view(), name='platform-list'),
    path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
    path('review/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),
]
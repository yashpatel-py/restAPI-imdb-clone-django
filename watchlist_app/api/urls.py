from django.urls import path, include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('streams', views.streamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name="movie-detail"),
    path('list2/', views.WatchLists.as_view(), name="watch-list"),

    path("", include(router.urls)),

    path('stream/', views.StreamPlatformAV.as_view(), name='platform-list'),
    # path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),

    # path('review/', views.ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name="review-detail")

    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name="streamplatform-detail"),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),


    path('reviews/', views.UserReview.as_view(), name="user-review-detail"),
]
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', views.registration_view, name="register"),
    path('logout/', views.logOut_view, name="logout"),
]
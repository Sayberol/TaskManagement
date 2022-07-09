# from django.contrib.auth import views
from . import views
from django.urls import path


urlpatterns = [
    # path('login', views.LoginView.as_view(), name='login'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
from . import views
from django.urls import path


urlpatterns = [
    path('update_password', views.UpdatePasswordView.as_view(), name='update_password'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
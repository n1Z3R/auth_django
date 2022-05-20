from django.contrib import admin
from django.urls import path

from auth_app.views import RegisterAPIView, LoginAPIView, LogoutAPIView, UserAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view())
]

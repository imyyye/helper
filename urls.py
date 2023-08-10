from django.urls import path
from .views import RegisterView, LoginView #로그인

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()), #로그인
]
from django.urls import path
from user import views


urlpatterns = [
    path('users/', views.UserCreate.as_view()),
]

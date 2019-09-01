from django.urls import path, re_path
from banks import views


urlpatterns = [
    re_path(r'^banks/?$', views.BankList.as_view()),
]

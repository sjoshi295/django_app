from django.urls import path
from banks import views


urlpatterns = [
    path('banks/<str:ifsc>/', views.BankUsingIFSC.as_view()),
    path('banks/<str:bank_name>/<str:city>/', views.BankListUsingNameCity.as_view()),
]

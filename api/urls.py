from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "user"


# 汎用APIViewを継承した場合
urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
]
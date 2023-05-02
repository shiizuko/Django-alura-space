from django.urls import path
from apps.users.views import login, register, logout

urlpatterns = [
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
]

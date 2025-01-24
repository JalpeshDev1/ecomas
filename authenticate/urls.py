from django.urls import path
from .views import *

#URLS regarding user authentications
urlpatterns = [
    path("register", Register.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
]
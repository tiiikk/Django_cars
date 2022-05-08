from django.urls import path, include
from . import views

app_name = 'auth'
urlpatterns = [
    path('register', views.register, name='register'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("send_email/", views.send_email),
]

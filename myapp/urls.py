from django.urls import path 
from . import views

urlpatterns = [
    path('http_server', views.http_server, name='http-server'),
]

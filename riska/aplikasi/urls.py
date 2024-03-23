from django.urls import path
from . import views

urlpatterns = [
    path ('', views.riska),
    path ('index/', views.index),
]     
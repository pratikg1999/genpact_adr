from django.urls import path

from . import views

urlpatterns = [
    path('naranjo', views.naranjo, name='naranjo'),
]
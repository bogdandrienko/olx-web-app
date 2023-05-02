from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home),
    path('json/', views.get_json),

    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.login),

    path('ad/detail/', views.login),
    path('ad/create/', views.login),
    path('ad/change/', views.login),
    path('ad/delete/', views.login),
]

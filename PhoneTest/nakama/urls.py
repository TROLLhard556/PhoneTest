from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('profile/', views.profile),
    path('login/', views.login),
    path('register/', views.register),
    path('forgotpw/', views.forgotpw),
    path('blank/', views.blank),
]

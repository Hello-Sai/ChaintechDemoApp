from django.urls import path

from app import views



urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('records',views.records)
]
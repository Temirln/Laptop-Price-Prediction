from django.contrib import admin
from django.urls import path

from laptops.views import predict,index

# app_name = 'predict'

urlpatterns = [
    path('predict/',predict, name="predictlaptop"),
    path('',index, name="home")
]

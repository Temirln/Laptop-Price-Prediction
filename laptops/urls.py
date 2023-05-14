from django.contrib import admin
from django.urls import path

from laptops.views import predict,index,predict_only_new
from laptops.views import LaptopAPIView

# app_name = 'predict'

urlpatterns = [
    path('predict/',predict, name="predictlaptop"),
    path('predict_new/',predict_only_new,name="predict_only_new"),
    path('',index, name="home"),
    path('api/v1/laptop_price/',LaptopAPIView.as_view())
]

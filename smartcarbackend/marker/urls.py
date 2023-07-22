from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index),
    path('timeremain',views.time_remain),
    path('alarm',views.alarm_marker),
    path('data',views.data),
]
from django.urls import path
from . import views


urlpatterns = [
    path('get',views.get_data_by_id),
    path('post',views.write_data),
]
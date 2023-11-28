from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('weather_city/', views.send_weather_city, name='weather_city'),
    path('return_weather/', views.return_weather_partial, name='return_weather')
]
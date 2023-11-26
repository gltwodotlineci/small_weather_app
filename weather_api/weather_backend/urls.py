from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('city2/', views.send_city2, name='send_city')
]
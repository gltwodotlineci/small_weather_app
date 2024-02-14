from django.urls import path, include
from rest_framework import routers
from . import views

from .views import BlogPostAPI


# Creating a router where we can call multiple urls
router = routers.DefaultRouter()
router.register(r'api_blg_posts', BlogPostAPI, basename='blog_post_api')


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('weather_city/', views.send_weather_city, name='weather_city'),
    path('return_weather/', views.return_weather_partial, name='return_weather'),
    path('products/', views.selling_products, name='selling_products')
]

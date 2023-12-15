from django.urls import path, include
from . import views
#from .views import BlogPostAPI
from rest_framework import routers

'''
# Creating a router where we can call multiple urls
router = routers.DefaultRouter()
router.register('blog_posts', BlogPostAPI, basename='blog_post_api')
'''

urlpatterns = [
    path('', views.home, name='home'),
    path('weather_city/', views.send_weather_city, name='weather_city'),
    path('return_weather/', views.return_weather_partial, name='return_weather'),
    #path('api/', include(router.urls))
]

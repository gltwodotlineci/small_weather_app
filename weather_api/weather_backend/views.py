from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Configuration, BlogPost
from dateutil.relativedelta import relativedelta
from .serializers import CitydayValidator
from cryptography.fernet import Fernet
from rest_framework import viewsets
from rest_framework.views import APIView

import requests, datetime, os


def decripting_api_key():
    # searching the encryption key
    key=os.environ.get('ENCRIPTION_KEY').encode()
    #Searching the encrypted api key from model
    api_key_encripted = Configuration.objects.all().last().weather_api_key.encode()
    f = Fernet(key)
    return f.decrypt(api_key_encripted).decode()


def home(request):
    return render(request, 'general/home.html', {})


#Sending the base form
def send_weather_city(request):
    return render(request, 'partials/weather_form.html', {})

def return_weather_partial(request):
     # The testing key example case (api non encrypted)
    api_key = decripting_api_key()

    city, added_days, day = "Paris", 0, 0

    #Geting the data from post
    if request.method == "POST":
        city_day_validator = CitydayValidator(data=request.POST)
        if not city_day_validator.is_valid():
            #if the data sent are not validated from the serializer
            return render(request,'base/home.html',{
                'message': f"Enter the right city name!"
            })

        #calling the data from the validator
        city = city_day_validator.validated_data['city']
        added_days = city_day_validator.validated_data['day']
    # creating the url with the link + api + town
    url_data = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={day}&aqi=no&alerts=no'
    day_choosed = timezone.localdate() + relativedelta(days=added_days)

    response = requests.get(url_data).json()#.format(api_key, town, day)).json()
    response['date_chosed'] = day_choosed
    return render(request, 'partials/return_weather.html', {'response': response})


# Starting the Blog posts API creation

class BlogPostAPI(viewsets.ViewSet):
    # sending list of blog posts
    def list(self, request):
        blog_posts = BlogPost.objects.all()
        return render(request, 'partials_blog_posts/blog_posts.html',{'blog_posts': blog_posts})

    # Method for creating a post on the blog
    def create(self,request):
        post_data = request.data
        data ={
            'title': post_data.get('title'),
            'body': post_data.get('body'),
            'author': post_data.get('author')
        }
        #data = post_data.get()
        BlogPost.objects.create(**data)
        return HttpResponseRedirect('api/blog_posts/')

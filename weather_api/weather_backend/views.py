from django.shortcuts import render
import datetime
import requests

def home(request):
    #api_key = open("/home/glen/Documents/p_doc/projects/weather_proj/weather/weather_api/weather_backend/API_KEY_WEATHER", "r").read()
    api_key = '31ff1ed1c68f4655b5b200134230510'
    town = "Tirana"
    # creating the url with the link + api + town
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={town}"
    return render(request, 'base/home.html', {})
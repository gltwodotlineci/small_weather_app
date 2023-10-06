from django.shortcuts import render
import datetime
import requests

def home(request):
    #api_key = open("/home/glen/Documents/p_doc/projects/weather_proj/weather/weather_api/weather_backend/API_KEY_WEATHER", "r").read()
    api_key = '31ff1ed1c68f4655b5b200134230510'
    town = "Tirana"
    day = 2
    # creating the url with the link + api + town
    url_data = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={town}&days={day}&aqi=no&alerts=no"

    response = requests.get(url_data).json()#.format(api_key, town, day)).json()

    return render(request, 'base/home.html', {'response': response})

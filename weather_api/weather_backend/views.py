from django.shortcuts import render
import datetime
import requests
#from .serializers import CitydayValidator


def home(request):
    #api_key = open("/home/glen/Documents/p_doc/projects/weather_proj/weather/weather_api/weather_backend/API_KEY_WEATHER", "r").read()
    api_key = '31ff1ed1c68f4655b5b200134230510'
    #calling the data from the validator
    '''
    city_date_validator = CityDayValidator(data=request.POST)
    if not city_date_validator:
        #if the data sent are not validated from the serializer
        return render(request,'',{
            'message': f"Enter the right city name!"
        })
    
    #If the data are validated:
    validated_data = city_date_validator.validated_data
    '''
    city1, day = "Paris", 0

    #Geting the data from post
    if request.method == "POST":
        city1 = request.POST['city1']
        day = request.POST['first_choice_day']



    # creating the url with the link + api + town
    #url_data = f"http://api.weatherapi.com/v1/current.json?key=31ff1ed1c68f4655b5b200134230510&q=Paris&days=1&aqi=no&alerts=no"
    url_data = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city1}&days={day}&aqi=no&alerts=no'
    response = requests.get(url_data).json()#.format(api_key, town, day)).json()

    return render(request, 'base/home0.html', {'response': response})

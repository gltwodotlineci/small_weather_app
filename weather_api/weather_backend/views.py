from django.shortcuts import render
from django.utils import timezone

from dateutil.relativedelta import relativedelta
from .serializers import CitydayValidator, SecondCityValidator
from cryptography.fernet import Fernet

import requests, datetime, os
#from .serializers import CitydayValidator

def home(request):
    # searching for th api key from .env
    # Generating a key for Fernet and passing the fonction to f
    '''
    # Geting the encripted key from .env and decripte it.
    encripted_api_key = os.environ.get('encripted_api_key')
    api_key = f.decrypt(encripted_api_key).decode()
    '''

    # The testing key example case (api non encrypted)
    api_key = os.environ.get('W_API_KEY')

    city1, added_days, day = "Paris", 0, 0

    #Geting the data from post
    if request.method == "POST":

        city_day_validator = CitydayValidator(data=request.POST)
        if not city_day_validator.is_valid():
            #if the data sent are not validated from the serializer
            return render(request,'base/home.html',{
                'message': f"Enter the right city name!"
            })

        #calling the data from the validator
        city1 = city_day_validator.validated_data['city1']
        added_days = city_day_validator.validated_data['day']
    # creating the url with the link + api + town
    #url_data = f"http://api.weatherapi.com/v1/current.json?key=31ff1ed1c68f4655b5b200134230510&q=Paris&days=1&aqi=no&alerts=no"
    url_data = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city1}&days={day}&aqi=no&alerts=no'
    day_choosed = timezone.localdate() + relativedelta(days=added_days)

    response = requests.get(url_data).json()#.format(api_key, town, day)).json()
    response['date_chosed'] = day_choosed

    return render(request, 'general/home.html', {'response': response})


def send_city2(request):
    city2, added_days, day2 = "Paris", 0, 0
    #Geting the api
    api_key = os.environ.get('W_API_KEY')
    if request.method == "POST":
        city_day_validator = SecondCityValidator(data=request.POST)
        if not city_day_validator.is_valid():
            #if the data sent are not validated from the serializer
            return render(request,'general/home.html',{
                'message': f"Enter the right city name!"
            })

        #calling the data from the validator
        city2 = city_day_validator.validated_data['city2']
        added_days = city_day_validator.validated_data['day2']

    # creating the url with the link + api + town
    #url_data = f"http://api.weatherapi.com/v1/current.json?key=31ff1ed1c68f4655b5b200134230510&q=Paris&days=1&aqi=no&alerts=no"
    url_data = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city2}&days={added_days}&aqi=no&alerts=no'
    day_choosed = timezone.localdate() + relativedelta(days=added_days)

    response = requests.get(url_data).json()#.format(api_key, town, day)).json()
    response['date_chosed'] = day_choosed

    return render(request, 'general/city2.html', {'response': response})


'''
def send_city(request):
    city_dict = {
        'cities': ['city2','city3','city4'],
        'days': ['day2','day3','day4'],
        'city_nb': [2,3,4],
        'nb_text': ['second','third','fourth'],
        'div': ['city_here2','city_here3','city_here4']
    }
    if request.GET.get('hide') == False:
        return render(request, 'general/home.html', context=city_dict)
    return render(request, 'general/city2.html', context=city_dict)
'''

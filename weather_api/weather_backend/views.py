from django.shortcuts import render
from django.utils import timezone

from dateutil.relativedelta import relativedelta
from .serializers import CitydayValidator
from cryptography.fernet import Fernet

import requests, datetime, os
#from .serializers import CitydayValidator
from django.conf import settings

def home(request):
    # searching for th api key from .env
    # Generating a key for Fernet and passing the fonction to f
    key = Fernet.generate_key()
    f = Fernet(key)

    # The testing key example case (api non encrypted)
    api_key = os.environ.get('W_API_KEY')

    '''
    # Geting the encripted key from .env and decripte it.
    encripted_api_key = os.environ.get('encripted_api_key')
    api_key = f.decrypt(encripted_api_key).decode()
    '''

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
    city1, added_days, day = "Paris", 0, 0

    #Geting the data from post
    if request.method == "POST":

        city_day_validator = CitydayValidator(data=request.POST)
        if not city_day_validator.is_valid():
            #if the data sent are not validated from the serializer
            print("nnnnnnnnnnnn oooo ooo nn")
            return render(request,'base/home0.html',{
                'message': f"Enter the right city name!"
            })


        city1 = city_day_validator.validated_data['city1']
        added_days = city_day_validator.validated_data['day']
    # creating the url with the link + api + town
    #url_data = f"http://api.weatherapi.com/v1/current.json?key=31ff1ed1c68f4655b5b200134230510&q=Paris&days=1&aqi=no&alerts=no"
    url_data = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city1}&days={day}&aqi=no&alerts=no'
    day_choosed = timezone.localdate() + relativedelta(days=added_days)

    response = requests.get(url_data).json()#.format(api_key, town, day)).json()
    response['date_chosed'] = day_choosed

    return render(request, 'general/home.html', {'response': response})


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
    return render(request, 'general/city_weather.html', context=city_dict)

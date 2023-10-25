from django.db import models
import os, uuid
from solo.models import SingletonModel
#We'll use configuration for the time zone and for
#the api_key
class Configuration(SingletonModel):
    time_zone = models.CharField(
        default="Europe/Paris",
        max_length=50
    )
    weather_api_key = models.CharField(max_length=150, blank=True, null=True)
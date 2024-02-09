import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from .models import Customuser
from weather_backend.models import BlogPost


#Serializer for the sign up data
class SignUpValidator(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True,required=True)
    passowrd = password2

    def validate_password1(self, value):
        print(f"Entering password 1 ---------")
        validators.validate_password(password=value)
        return value

    def validate_paxxord2(self, value):
        print(f"Entering password 2 ---------")
        validators.validate_password(password=value)
        return value

'''        
        if value == self.passowrd:
            return True
        raise serializers.ValidationError(f"Erreur de saisie les mot de passes doivent être identiques")
'''

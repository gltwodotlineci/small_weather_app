from django.shortcuts import render
from .models import Customuser
from serializers import SignUpValidator


def signup(request):
    signup_validator = SignUpValidator(data=request.POST)
    if not signup_validator.is_valid():
        print(f'Error in signup form: {signup_validator.errors}')
        return render(request, 'users/signup.html', {})
    username= signup_validator.get('username')
    email = signup_validator.get('email')
    password = signup_validator.get('password')
    #creating the User
    Customuser.objects.create(username=username, email= email, password=password, pseudo=username)

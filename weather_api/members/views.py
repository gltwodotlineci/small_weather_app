from django.shortcuts import render
from .models import Customuser
from .serializers import SignUpValidator

def sign_up(request):
    signup_validator = SignUpValidator(data=request.POST)
    if not signup_validator.is_valid():
        print(f'Error in signup form: {signup_validator.errors}')
        return render(request, 'users/signup.html', {})
    signup_validator = None
    username= signup_validator.get('username')
    email = signup_validator.get('email')
    password1 = signup_validator.get('password1')
    password2 = signup_validator.get('password2')

    if password1 != password2:
        return render(request, 'users/signup.html', {'message:' f"The passwords shuld not be differents!"})
    #creating the User
    Customuser.objects.create(username=username, email= email, password=password1, pseudo=username)
    return render(request, 'general/home.html', {})
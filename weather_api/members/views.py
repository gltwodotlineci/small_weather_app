from django.shortcuts import render
from .models import Customuser


def signup(request):
    return render(request, 'users/signup.html', {})

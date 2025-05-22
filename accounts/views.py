from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def Register(request):
    return render(request, 'Account/registration.html')

def Login(request):
    return render(request, 'Account/login.html')

def otp(request):
    return render(request, 'Account/otp.html')

def forget(request):
    return render(request, 'Account/forget.html')
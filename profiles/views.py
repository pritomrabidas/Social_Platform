from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'Profiles/home.html')


def profile(requst):
    return render(requst, 'Profiles/profile.html')

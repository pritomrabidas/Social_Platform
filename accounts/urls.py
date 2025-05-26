from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('otp/', otp, name='otp'),
    path('forget/', forget, name='forget'),
    path('resend_otp/', resend_otp, name='resend_otp'),
]
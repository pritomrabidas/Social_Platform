from django.urls import path
from .views import *

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('otp/', otp, name='otp'),
    path('resend_otp/', resend_otp, name='resend_otp'),
    path('forget_email/', forget_email, name='forget_email'),
    path('forget_otp/', forget_otp, name='forget_otp'),
    path('forget/', forget, name='forget'),
]
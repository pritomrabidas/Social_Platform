from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from config.settings import EMAIL_HOST_USER
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.
def Register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        city = request.POST.get('city')
        country = request.POST.get('country')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'Account/registration.html')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'Account/registration.html')

        if password == confirm_password:
            otp = random.randint(1000, 9999)
            user = CustomUser.objects.create_user(
                fullname=fullname,username=username,
                email=email,city=city,
                country=country,password=password,
                otp=otp,
                )
            user.save()
            registration_Email(otp, email)
            request.session['email'] = email
            return redirect('otp') 
        else:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Account/registration.html') 

    return render(request, 'Account/registration.html')

def registration_Email(otp, email):
    subject = "Welcome to Our Website"
    message = f"Thank you for registering with us. Your OTP is: {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def otp(request):
    otp = request.POST.get('otp')
    if request.method == 'POST':
        if otp:
            try:
                user = CustomUser.objects.get(otp=otp)
                user.is_varified = True
                user.save()
                return redirect('login')
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid OTP. Please try again.")
                return render(request, 'Account/otp.html')
        else:
            messages.error(request, "Please enter the OTP.")
            return render(request, 'Account/otp.html')
    return render(request, 'Account/otp.html')

def resend_otp(request):
    email = request.session.get('email')
    if email:
        try:
            user = CustomUser.objects.get(email=email)
            otp = random.randint(1000, 9999)
            user.otp = otp
            user.save()
            registration_Email(otp, email)
            messages.success(request, "OTP has been resent to your email.")
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
    else:
        messages.error(request, "No email found in session.")
    return redirect('otp')

def Login(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        user = None
        if CustomUser.objects.filter(email=identifier).exists():
            username = CustomUser.objects.get(email=identifier).username
            user = authenticate(request, username=username, password=password)

        elif CustomUser.objects.filter(username=identifier).exists():
            user = authenticate(request, username=identifier, password=password)

        if user is not None:
            if user.is_varified:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Please verify your account first.")
                return render(request, 'Account/login.html')

        messages.error(request, "Invalid login credentials.")

    return render(request, 'Account/login.html')



def forget(request):
    return render(request, 'Account/forget.html')
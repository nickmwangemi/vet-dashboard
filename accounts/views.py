from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import CustomUser
from .models import CustomUser
from django.contrib.auth import authenticate
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Get form values
        full_name = request.POST['full_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if CustomUser.objects.filter(mobile_number=mobile_number).exists():
                messages.error(request, 'That mobile number is already in use')
                return redirect('accounts:register')
            else:
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already taken')
                    return redirect('accounts:register')
                else:
                    # Looks good
                    user = CustomUser()
                    user.full_name = full_name
                    user.email = email
                    user.mobile_number = mobile_number
                    user.password = password

                    user = CustomUser.objects.create_user(
                        full_name=full_name, email=email, mobile_number=mobile_number, password=password)
                    user.save()

                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('dashboard:index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('accounts:login')


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'user': user
        }

        return render(request, 'accounts/profile.html', context)

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required

def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'), )
        print(user)
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                print(user_type)
                return redirect('hod_home')
            elif user_type == '2':
                print(user_type)
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                print(user_type)
                return HttpResponse('This is Student Panel')
            else:
                messages.error(request, 'Email and Password Are Invalid !')
                return redirect('login')
        else:
            print('redirected')
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')
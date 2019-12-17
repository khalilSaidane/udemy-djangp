from django.contrib import messages
from django.shortcuts import render,redirect


def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing Error Messages')
        return redirect('register')
    return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

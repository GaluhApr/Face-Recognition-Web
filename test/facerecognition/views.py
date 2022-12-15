from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def coba(request):
    return render(request, 'coba.html')

def loginview(request):
    if request.method == 'POST':
        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)
    
        if user is not None:
            login(request, user)
        else:
            return redirect('login')   
        
        return redirect('dashboard')
    
    return render(request, 'index.html')
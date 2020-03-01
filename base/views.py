from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index_page(request):
    return render(request, 'index.html', {})


def security_page(request):
    return render(request, 'security.html', {})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request, user)
        else:
            pass
        return redirect('index')


def logout_page(request):
    logout(request)
    return redirect('index')

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgotpw(request):
    return render(request, 'forgotpw.html')

def blank(request):
    return render(request, 'blank.html')

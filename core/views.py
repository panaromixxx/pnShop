from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request, 'core/signin.html')

def signup(request):
    return render(request, 'core/signup.html')

def profile(request):
    return render(request, 'core/profile.html')
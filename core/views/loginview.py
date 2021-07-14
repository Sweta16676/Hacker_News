from django.http import HttpResponse
from django.shortcuts import render,redirect


def home(request):
    return render(request, 'static.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'sign up.html')
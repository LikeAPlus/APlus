from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.models import User

# Create your views here.
def sign_in(request):
    return render(request, 'users/sign_in.html')

def create(request):
    return render(request, 'users/create.html')

def create_user(request):
    return render(request, 'users/create.html')

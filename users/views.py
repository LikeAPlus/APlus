from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.models import User
from .forms import SignupForm, SigninForm
from django.contrib.auth.views import login as auth_login


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            return redirect('/')  # default : '/accounts/login'
    else:
        form = SignupForm()


    ctx = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', ctx)


def sign_in(request):
    return auth_login(request,
        authentication_form=SigninForm,
        template_name='users/sign_in.html',
    )


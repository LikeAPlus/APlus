from django.contrib.auth import logout
from django.contrib.auth.views import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignupForm, SigninForm


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            return redirect('/qnas')  # default : '/accounts/login'
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


def log_out(request):
    logout(request)
    return redirect('/')

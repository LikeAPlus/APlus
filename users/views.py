from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

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
    providers = []
    for provider in get_providers():
        # social_app속성은 provider에는 없는 속성입니다.
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return auth_login(request,
                      authentication_form=SigninForm,
                      template_name='users/sign_in.html',
                      extra_context={'providers': providers})


def log_out(request):
    logout(request)
    return redirect('/')

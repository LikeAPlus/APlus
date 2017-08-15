from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_in),
    url(r'^sign_in/$', views.sign_in),
    url(r'^signup/$', views.sign_up),
    url(r'^u/create$', views.create),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_in),
    url(r'^sign_in$', views.sign_in),
    url(r'^u/create$', views.create),
]

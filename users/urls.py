from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_in),
    url(r'^signin/$', views.sign_in, name='signin'),
    url(r'^signup/$', views.sign_up, name='signup'),

]

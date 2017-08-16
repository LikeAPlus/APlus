from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^signin/$', views.sign_in, name='signin'),
    url(r'^logout/$', views.log_out, name='logout'),
]

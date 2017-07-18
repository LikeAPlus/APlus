from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index)
    url(r'^q/create/$', views.create),
    url(r'^q/create_question/$', views.create_question),
]

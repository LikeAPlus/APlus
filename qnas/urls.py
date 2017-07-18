from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^qnas/(?P<major_name>[a-zA-Z]+)/$', views.index),
    url(r'^qnas/(?P<major_name>[a-zA-Z]+)/(?P<course_name>[a-zA-Z]+)/$', views.index),
    url(r'^q/create/$', views.create),
    url(r'^q/create_question$', views.create_question),
    url(r'^q/read/(?P<post_id>.+)/$', views.read),
    url(r'^a/create_answer$', views.create_answer),
]

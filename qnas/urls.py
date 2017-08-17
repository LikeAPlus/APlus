from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='qnas_all'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete_question$', views.delete_question, name='delete_question'),
    url(r'^read/(?P<post_id>.+)$', views.read, name='read'),
    url(r'^create_answer$', views.create_answer, name='create_answer'),
    url(r'^delete_answer$', views.delete_answer, name='delete_answer'),

    url(r'^read_courses/(?P<major_name>[ㄱ-ㅎㅏ-ㅣ가-힣]+)', views.read_courses, name='read_courses'),
    url(r'^(?P<major_name>[a-zA-Z]+)/(?P<course_name>[a-zA-Z]+)', views.index),
    url(r'^(?P<major_name>[a-zA-Z]+)', views.index),
]

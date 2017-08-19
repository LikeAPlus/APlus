from django.shortcuts import render
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


def root(request):
    return render(request, 'APlus/root.html')


urlpatterns = [
    url(r'^$', root, name='root'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('allauth.urls')),
    url(r'^qnas/', include('qnas.urls', namespace='qnas')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

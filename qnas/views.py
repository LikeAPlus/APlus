# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'qnas/index.html', context)

def create(request):
    return render(request, 'qnas/create.html')

def create_question(request):
    title = request.POST['title']
    return HttpResponseRedirect("/")

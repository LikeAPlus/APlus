# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from .models import Major, Course, Post, Comment

# Create your views here.
def index(request, major_name = '', course_name = ''):
    try:
        major = Major.objects.get(name = major_name)
        course = Course.objects.get(name = course_name)
        posts = Post.objects.filter(major = major, course = course)
    except:
        try:
            major = Major.objects.get(name = major_name)
            posts = Post.objects.filter(major = major)
        except:
            posts = Post.objects.order_by("id").reverse()

    majors = Major.objects.all()
    courses = Course.objects.all()
    context = {'posts': posts, 'majors': majors, 'courses': courses}
    return render(request, 'qnas/index.html', context)

def create(request):
    majors = Major.objects.all()
    courses = Course.objects.all()
    context = {'majors': majors, 'courses': courses}

    return render(request, 'qnas/create.html', context)

def create_question(request):
    major = Major.objects.get(id = request.POST['major'])
    course = Course.objects.get(id = request.POST['course'])
    title = request.POST['title']
    content = request.POST['content']

    post = Post(major = major, course = course, title = title, content = content)
    post.save()

    return HttpResponseRedirect("/q/read/{}".format(post.id))

def delete_question(request):
    post = Post.objects.get(id = request.POST['post_id'])
    post.delete()

    return HttpResponseRedirect("/")


def read(request, post_id):
    post = Post.objects.get(id = post_id)
    comments = Comment.objects.filter(post = post)
    context = {'post': post, 'comments': comments}

    return render(request, 'qnas/read.html', context)

def create_answer(request):
    post = Post.objects.get(id = request.POST['post_id'])
    content = request.POST['content']

    comment = Comment(post = post, content = content)
    comment.save()

    return HttpResponseRedirect("/q/read/{}".format(post.id))

def delete_answer(request):
    post_id = request.POST['post_id']
    comment = Comment.objects.get(id = request.POST['comment_id'])
    comment.delete()

    return HttpResponseRedirect("/q/read/{}".format(post_id))

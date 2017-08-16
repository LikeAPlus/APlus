# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Major, Course, Post, Comment


# Create your views here.
def index(request, major_name='', course_name=''):
    if major_name != '' and course_name != '':
        major = Major.objects.get(e_name=major_name)
        course = Course.objects.get(e_name=course_name)
        posts = Post.objects.filter(major=major, course=course)
    elif major_name != '':
        major = Major.objects.get(e_name=major_name)
        posts = Post.objects.filter(major=major)
    else:
        posts = Post.objects.order_by("id").reverse()

    majors = Major.objects.all()
    if major_name != '':
        courses = Course.objects.filter(major=major)
    else:
        courses = ''

    context = {'posts': posts, 'majors': majors, 'courses': courses, 'major_name': major_name,
               'course_name': course_name}
    return render(request, 'qnas/index.html', context)


def read_courses(request, major_name):
    major = Major.objects.get(name=major_name)
    courses = Course.objects.filter(major=major)
    courses_info = []
    for c in courses:
        course = {}
        course['id'] = c.id
        course['name'] = c.name
        courses_info.append(course)

    return JsonResponse({'courses': courses_info})


@login_required(login_url='/users/signin/')
def create(request):
    if request.method == 'POST':
        major = Major.objects.get(id=request.POST['major'])
        course = Course.objects.get(id=request.POST['course'])
        title = request.POST['title']
        content = request.POST['content']

        post = Post(user=request.user, major=major, course=course, title=title, content=content)
        post.save()

        return redirect('qnas:read', post.id)
    else:

        majors = Major.objects.all()
        courses = Course.objects.all()
        context = {'majors': majors, 'courses': courses}

        return render(request, 'qnas/create.html', context)


def delete_question(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.delete()

    return redirect("/qnas")


def read(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}

    return render(request, 'qnas/read.html', context)


def create_answer(request):
    post = Post.objects.get(id=request.POST['post_id'])
    content = request.POST['content']

    comment = Comment(user=request.user, post=post, content=content)
    comment.save()

    return redirect('qnas:read', post.id)


def delete_answer(request):
    post_id = request.POST['post_id']
    comment = Comment.objects.get(id=request.POST['comment_id'])
    comment.delete()

    return redirect('qnas:read', post_id)

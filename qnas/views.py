# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import PostForm
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Major, Course, Post, Comment


# Create your views here.
def index(request, major_name='', course_name=''):
    if major_name != '' and course_name != '':
        major = Major.objects.get(e_name=major_name)
        course = Course.objects.get(e_name=course_name)
        posts = Post.objects.filter(major=major, course=course).order_by("-id")
    elif major_name != '':
        major = Major.objects.get(e_name=major_name)
        posts = Post.objects.filter(major=major).order_by("-id")
    else:
        posts = Post.objects.order_by("-id")

    pop_posts = posts.annotate(num_comments=Count('comment')).order_by('-num_comments')

    majors = Major.objects.all()
    if major_name != '':
        courses = Course.objects.filter(major=major)
    else:
        courses = ''

    context = {'posts': posts, 'pop_posts': pop_posts, 'majors': majors, 'courses': courses, 'major_name': major_name,
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


# @login_required(login_url='/users/signin/')
# def create(request):
#     if request.method == 'POST':
#         major = Major.objects.get(id=request.POST['major'])
#         course = Course.objects.get(id=request.POST['course'])
#         title = request.POST['title']
#         content = request.POST['content']
#         if request.POST['image'] != '':
#             image = request.FILES['image']
#             post = Post(user=request.user, major=major, course=course, title=title, content=content, image=image)
#         else:
#             post = Post(user=request.user, major=major, course=course, title=title, content=content)
#         post.save()
#
#         return redirect('qnas:read', post.id)
#
#     else:
#
#         majors = Major.objects.all()
#         courses = Course.objects.all()
#         context = {'majors': majors, 'courses': courses}
#
#         return render(request, 'qnas/create.html', context)

def create1(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('qnas:read', obj.id)
    else:
        form = PostForm()

    ctx = {
        'form': form
    }
    return render(request, 'qnas/create.html', ctx)

def delete_question(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.delete()

    return redirect("/qnas")


def read(request, post_id):
    post = Post.objects.get(id=post_id)
    post.view_count += 1
    post.save()
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

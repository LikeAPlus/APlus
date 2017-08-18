# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=20)
    e_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    major = models.ForeignKey(Major)
    name = models.CharField(max_length=20)
    e_name = models.CharField(max_length=20)
    professor = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    major = models.ForeignKey(Major)
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=123)
    content = models.TextField()
    image = models.ImageField(upload_to='qnas/%Y/%m/%d', null=True, blank=True)
    view_count = models.IntegerField(default=0)
    # like_count = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)
    major = models.ForeignKey(Major)
    professor = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    major = models.ForeignKey(Major)
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=123)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()

    def __str__(self):
        return self.content

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)
    school = models.ForeignKey(School)
    professor = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    school = models.ForeignKey(School)
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=123)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()

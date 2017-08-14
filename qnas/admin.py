# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Major, Course, Post, Comment

# Register your models here.
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(Comment)

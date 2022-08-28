# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subject,Webpage,AcessRecord 

# Register your models here.

admin.site.register(Subject)
admin.site.register(Webpage)
admin.site.register(AcessRecord)

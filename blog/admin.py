# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Post_new

#admin.site.register(Post)

# Define the admin class
class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'text')

# Register the admin class with the associated model
admin.site.register(Post, PostAdmin)

@admin.register(Post_new)
class PersonAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('author', 'title', 'text')

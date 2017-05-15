# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # this creates a slug off of the category name entered. Python User Group becomes python_user_group

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url') # it displays the fields in the tuple as columns side by side

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


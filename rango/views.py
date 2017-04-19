# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Rango says welcome partner!!")

def index(request):
    html1 = "Rango says hey there partner!" '<a href="/rango/about">About</a>'
    return HttpResponse(html1)

def about(request):
    html2 = "Rango says here is the about page" '<a href="/rango/">Home</a>'

    return HttpResponse(html2)


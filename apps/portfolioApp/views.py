# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    print "in portfolio index"
    return render(request, 'portfolioApp/index.html')

def testimonial(request):
    print "testimonial view"
    return render(request, 'portfolioApp/testimonial.html')

def projects(request):
    print "request view"
    return render(request, 'portfolioApp/projects.html')

def aboutme(request):
    print "aboutme"
    return render(request, 'portfolioApp/aboutme.html')
# Create your views here.

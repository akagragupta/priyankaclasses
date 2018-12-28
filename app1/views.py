# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'app1/About.html',{})

def admissions(request):
	return render(request,'app1/Admissions.html',{})

def contact(request):
	return render(request,'app1/Contact.html',{})

def curriculum(request):
	return render(request,'app1/Curriculum.html',{})

def fees(request):
	return render(request,'app1/Fees.html',{})
	
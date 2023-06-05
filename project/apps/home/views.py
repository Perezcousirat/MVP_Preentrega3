from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from . import forms



def index(request):
   
    return render(request, 'home/index.html')


  
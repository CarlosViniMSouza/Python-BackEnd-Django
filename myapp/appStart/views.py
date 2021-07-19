from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1> Hello, be welcome to my Site! </h1>')

# Okay, now, lets go to the Terminal writer 'python manage.py runserver' for generate the application's localhost
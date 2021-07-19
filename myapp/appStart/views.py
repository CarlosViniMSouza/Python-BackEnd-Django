from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Okay, now, lets go to the Terminal writer 'python manage.py runserver' for generate the application's localhost
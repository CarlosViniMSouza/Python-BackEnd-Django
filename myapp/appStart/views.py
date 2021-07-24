from django.shortcuts import render
from django.http import HttpResponse
#from .models import Feature

# Create your views here.
def index(request):
    #feature1 = Feature()
    #feature1.id = 0
    #feature1.name = "Django"
    #feature1.details = "Service in maintenance"
    return render(request, 'index.html') #, {'feature': feature1}

# Okay, now, lets go to the Terminal writer 'python manage.py runserver' for generate the application's localhost

def counter(request):
    text = request.POST['text']
    count_words = len(text.split())
    return render(request, 'counter.html', {'count': count_words})
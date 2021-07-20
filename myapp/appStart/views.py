from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    user = {
        'name': 'CarlosViniMSouza',
        'age': 20,
        'nationality': 'Brazilian',
        'college': 'Graduate'
    }
    return render(request, 'index.html', user)

# Okay, now, lets go to the Terminal writer 'python manage.py runserver' for generate the application's localhost

def counter(request):
    text = request.POST['text']
    count_words = len(text.split())
    return render(request, 'counter.html', {'count': count_words})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index')
]

# In this file, we can controller the routes in working on project.
# And to organize it better, we created a list of URLs
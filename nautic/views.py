from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request, *args, **kwargs):
    return render(request, "index.html")

def about(request, *args, **kwargs):
    return render(request, "about.html")

x = "Welcome home"
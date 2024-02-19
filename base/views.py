from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request, *args, **kwargs):
    return HttpResponse("wELCOME TO OUR HOME PAGE")

def about(reauest, *args, **kwargs):
    return HttpResponse("Welcome to our homepage")

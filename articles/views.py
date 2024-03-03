from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def articleview(request, *args, **kwargs):
    articles = Article.objects.all().order_by('date')
    
    return render(request, "articles/articles.html", {'articles':articles})

def article_detail(request,slug, *args, **kwargs):
    return HttpResponse(slug)
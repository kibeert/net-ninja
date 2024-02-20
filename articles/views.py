from django.shortcuts import render

# Create your views here.
def articleview(request, *args, **kwargs):
    return render(request, "articles/articles.html")
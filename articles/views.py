from django.shortcuts import render

# Create your views here.
def articlelist(request, *args, **kwargs):
    return render(request, "articles/article_list.html", {})
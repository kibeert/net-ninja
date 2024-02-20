from django.shortcuts import render

# Create your views here.
def article_view(request, *args, **kwargs):
    return render(request, "templates/article/article_list.html")
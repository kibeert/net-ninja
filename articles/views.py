from django.shortcuts import render

# Create your views here.
def atriclelist(request, *args, **kwargs):
    return render(request, 'artcles/article_list.html')

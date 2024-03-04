from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views import View

# Create your views here.
def articleview(request, *args, **kwargs):
    articles = Article.objects.all().order_by('date')
    
    return render(request, "articles/articles.html", {'articles':articles})

def article_detail(request, *args, **kwargs):
    return HttpResponse("Hello world")

from django.shortcuts import render, get_object_or_404
from .models import Article  # Make sure to import your Article model
from django.views import View

class ArticleDetailView(View):
    template_name = 'independent.html'  # Replace with your actual template name

    def get(self, request, slug):
        # Retrieve the article with the given slug or ID
        article = get_object_or_404(Article, slug=slug)

        # You can add additional logic here if needed

        # Render the article detail template with the article context
        return render(request, self.template_name, {'article': article})

from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import ArticleDetailView

urlpatterns = [
    path('article/', views.articleview, name='articles'),
    path('slug/', views.article_detail ,name="article-detail"),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    
]
urlpatterns += staticfiles_urlpatterns()

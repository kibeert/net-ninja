from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('article/', views.articleview, name='articles'),
    path('slug/', views.article_detail ,name="article-detail"),
    
]
urlpatterns += staticfiles_urlpatterns()

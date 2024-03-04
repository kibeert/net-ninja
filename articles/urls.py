from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'articles'

urlpatterns = [
    path('article/', views.articleview, name='articles'),
    path('slug/', views.article_detail ,name="article-detail"),
    path('', views.articleview, name="list"),
    path('<slug>/', views.article_detail, name="detail")

    
    
]
urlpatterns += staticfiles_urlpatterns()

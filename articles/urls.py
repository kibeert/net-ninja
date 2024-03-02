from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('article/', views.articleview, name='articles'),
    
]
urlpatterns += staticfiles_urlpatterns()

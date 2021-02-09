from django.shortcuts import render
from articles import models

# Create your views here.

def articleslist(request):

    articles = models.Article.title
    return render(request, 'articles/articleslist.html', {'articles':articles})
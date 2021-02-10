from django.shortcuts import render , HttpResponse
from articles import models

# Create your views here.

def articleslist(request):

    articles = models.Article.title
    return render(request, 'articles/articleslist.html', {'articles':articles})

def article_detail(request , slug):
    
    return HttpResponse(slug)
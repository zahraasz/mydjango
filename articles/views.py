from django.shortcuts import render
from articles import models

# Create your views here.
def articleslist(request):

    articles = models.Article
    # .object.all().order_by('date')
    artc = {'articles':articles}
    return  render(request , 'articles/articleslist.html', artc )

from django.urls import path 
from articles import views   #read views

app_name = "articles"
urlpatterns = [
    path('' , views.articleslist , name = "list"),
    path('<slug>' , views.article_detail , name = "detail"),
]



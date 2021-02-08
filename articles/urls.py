from django.urls import path 
from articles import views   #read views


urlpatterns = [
    path('' , views.articleslist),
]



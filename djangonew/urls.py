
from django.contrib import admin
from django.urls import path , include 
from djangonew import views   #read views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('about/' , views.about),
    path('' , views.home),
    path('articles/' , include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()   # ezafe kardane ye
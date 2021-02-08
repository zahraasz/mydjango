from django.contrib import admin
# from  articles import models
from . import models

# Register your models here.
admin.site.register(models.Article)
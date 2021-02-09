from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50)
    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add = True)
    # picture
    # author  # nevisandeh
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body
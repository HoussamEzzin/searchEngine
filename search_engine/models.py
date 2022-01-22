from django.db import models

# Create your models here.


class Article(models.Model):
    author = models.TextField()
    content = models.TextField()
    keywords = models.TextField()
    title = models.TextField()
    
    def _str_(self):
        return self.title
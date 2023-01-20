from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



# Create your models here.


class Category(models.Model):
    name =models.CharField(max_length=32)
    description=models.TextField(null= True, blank=True)
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        
        
    def __str__(self):
        return self.name
    
# A list of tuples.

   
        
        
class Article(models.Model):
    
    ARTICLE_TYPES = (
    ('UN', _('Unspecified')),
    ('TU', _('Tutorial')),
    ('RS', _('Research')),
    ('CO', _('Coding')),
    ('PY', _('Python'))
  )
    
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=ARTICLE_TYPES, default='UN')
    categories = models.ManyToManyField(to=Category, blank=True, related_name='categories')
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    


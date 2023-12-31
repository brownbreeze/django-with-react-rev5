from django.conf import settings
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True    
    
class Post(models.Model):
    pass 

class Comment(models.Model):
    pass

class Tag(models.Model):
    pass
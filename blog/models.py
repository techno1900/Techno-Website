from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    post_image  = models.ImageField(upload_to="blog/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    video = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)


    def __str__(self):
        return self.title
    

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'categories'





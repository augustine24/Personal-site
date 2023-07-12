from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)  # Add the pub_date field

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class SiteBackground(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    
class YourImageModel(models.Model):
    image = models.ImageField(upload_to='images/')



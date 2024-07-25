from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True,default=None, blank=True, unique=True)

    def __str__(self) -> str:
        return self.name

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='listings/', null=True, default=None, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    telephone_number = models.CharField(max_length=20, null=True)
    slug = models.SlugField(null=True,default=None, blank=True, unique=True)


    def __str__(self):
        return self.title
    

    

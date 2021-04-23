from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.item
    
    def get_absolute_url(self):
        return reverse('home')

# Create your models here.

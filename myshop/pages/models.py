from django.db import models
from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    price= models.CharField(max_length=255)
    sale = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
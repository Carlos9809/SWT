from django.db import models

# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length = 50)
    imagen = models.ImageField()
    autor = models.CharField(max_length = 30, default='anonymous')
    
   

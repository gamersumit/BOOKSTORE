
# Create your models here.
from django.db import models


# Create your models here.

class BookStore(models.Model):
    
    title = models.CharField(max_length = 100, unique=True, blank=False, null=False)
    author = models.CharField(max_length = 50,  blank=False, null=False)
    publication_year = models.PositiveIntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, blank=False, null=False)
    image = models.ImageField(upload_to = "books/", blank=True, null = True) 
   
    def __str__(self):
        return self.title
    

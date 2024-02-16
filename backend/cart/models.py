from django.db import models
from account.models import CustomUser
from bookstore.models import BookStore
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(BookStore, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    # Add any other fields you may need

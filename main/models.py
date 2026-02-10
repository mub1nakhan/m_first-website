from django.db import models

# Create your models here.

class Quote(models.Model):
    book_name = models.CharField(max_length=225)
    book_author = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.book_name} - {self.book_author}"
    
class Book(models.Model):
    name = models.CharField( max_length=250)
    author = models.CharField(max_length=250)
    price = models.IntegerField()
    ganre = models.CharField(max_length=224)
    read_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.author}" 
    
    
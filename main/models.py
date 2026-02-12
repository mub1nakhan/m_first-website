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
    
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    
    
    def __str__(self):
        return f"{self.name} - {self.year}"
    
    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"
    
    
class Book(models.Model):
    title = models.CharField( max_length=250)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)

    
    def __str__(self):
        return f"{self.title} - {self.author}" 
    
     
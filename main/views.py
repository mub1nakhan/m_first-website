from django.shortcuts import render,redirect
from .models import Book
from .models import Author
# Create your views here.


def mine_s(request):
    
    if request.method == "POST":
        title = request.POST.get("title")
        author_name = request.POST.get("author")
        
        author = Author.objects.filter(name__icontains = author_name).first()
        if not author:
            author= Author.objects.create(name=author_name,year=1967)
            
        book = Book.objects.create(
            title= title,
            author= author
        )
        return redirect("index")
    
    
    
    
    
    
    
    book = Book.objects.all()
    author = Author.objects.all()
    return render(request,"index.html", context={"books":book,"authors":author})


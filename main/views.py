from django.shortcuts import render

# Create your views here.


def mine_s(request):
    return render(request,"index.html")
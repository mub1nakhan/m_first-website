
from django.http import HttpResponse


def hello(request):
   return HttpResponse("Salomm Dunyo")

def bye(request):
    return HttpResponse("Xayr dunyo")
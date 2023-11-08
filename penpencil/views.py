from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jampandu(request):
    return HttpResponse('<h1>Hai jampandu How are you<h1/>(marqee)')

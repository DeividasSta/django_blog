from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def index(request):
    return render(request, 'articles/index.html')

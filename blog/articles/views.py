from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.order_by('-pub_date')
    context = {'articles': articles}

    return render(request, 'articles/index.html', context)


def details(request, a_id):
    article = Article.objects.get(pk=a_id)
    context = {'article': article}

    return render(request, 'articles/details.html', context)

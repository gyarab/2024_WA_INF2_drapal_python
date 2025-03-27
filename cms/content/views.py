from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

from .models import Article, Author, Category

# data = [
#     {
#         'title': 'web',
#         'link': 'https://www.gyarab.cz',
#     },
#     {
#         'title': 'web 2',
#         'link': 'https://www.youtube.com',
#     },
#     'Three',
#     'Four',
# ]

def home(request):
    articles = Article.objects.order_by('title')
    return render(request, 'content/home.html', {'articles': articles})
    
def article(request, id):
    article = Article.objects.get(pk=id)

    return render(request, 'content/article.html', {'article': article})

def author(request, id):
    author = Author.objects.get(pk=id)

    return render(request, 'content/author.html', {'author': author})

def category(request, id):
    category = Category.objects.get(pk=id)

    return render(request, 'content/category.html', {'category': category})
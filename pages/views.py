from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsPost

def news(request):
    news = NewsPost.objects.all().order_by('-created_at')[1:5]
    recentnews = NewsPost.objects.latest('created_at')
    context = {
        'title': 'Pages',
        'news' : news,
        'latest' : recentnews, 
    }
    return render(request, 'posts/news.html', context)
    

def article(request, id):
    news = NewsPost.objects.get(id=id)
    context = {
    'post' : news,
    'title': news.title,
    }
    return render(request, 'posts/article.html', context)
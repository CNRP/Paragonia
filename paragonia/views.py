from django.shortcuts import render
from django.http import HttpResponse
from pages.models import NewsPost
from .models import GuideSection
from .models import HomeSection

def index(request):
    recentnews = NewsPost.objects.latest('created_at')
    homesections = HomeSection.objects.all()
    context = {
        'title': 'Homepage',
        'latest' : recentnews, 
        'homesections' : homesections, 
    }
    return render(request, 'pages/home.html', context)

def guides(request):
    guides = GuideSection.objects.all()
    context = {
        'title': 'Pages',
        'guides' : guides,
    }
    return render(request, 'pages/guides.html', context)
    
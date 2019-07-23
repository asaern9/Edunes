from django.shortcuts import render, reverse
from django.views.generic import DetailView
from .models import News
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


class NewsDetail(DetailView):
    model = News
    template_name = 'blog/news_detail.html'


def arts_culture(request):
    return render(request, 'blog/arts_culture.html')


def business(request):
    return render(request, 'blog/business.html')


def entertainment(request):
    return render(request, 'blog/entertainment.html')


def fashion(request):
    return render(request, 'blog/fashion.html')


def health(request):
    return render(request, 'blog/health.html')


def politics(request):
    return render(request, 'blog/politics.html')


def sport(request):
    return render(request, 'blog/sport.html')


def tech(request):
    return render(request, 'blog/tech.html')


def contact(request):
    return render(request, 'blog/contact.html')

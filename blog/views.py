from django.shortcuts import render, reverse
from django.views.generic import DetailView
from .models import News
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


class NewsDetail(DetailView):
    model = News
    template_name = 'blog/news_detail.html'

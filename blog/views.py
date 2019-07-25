from django.shortcuts import render, reverse
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import News
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


class NewsDetail(DetailView):
    model = News
    template_name = 'blog/news_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsDetail, self).get_context_data(*args, **kwargs)
        context['related_post'] = News.objects.filter(category='politics').order_by('-id')[:4]
        return context


def arts_culture(request):
    arts = News.objects.all().filter(category='arts')
    context = {'arts': arts}
    return render(request, 'blog/arts_culture.html', context)


def business(request):
    bus = News.objects.all().filter(category='business')
    context = {'business': bus}
    return render(request, 'blog/business.html', context)


def entertainment(request):
    enter = News.objects.all().filter(category='entertainment')
    context = {'entertainment': enter}
    return render(request, 'blog/entertainment.html', context)


def fashion(request):
    fash = News.objects.all().filter(category='fashion')
    context = {'fashion': fash}
    return render(request, 'blog/fashion.html', context)


def health(request):
    heal = News.objects.all().filter(category='health')
    context = {'health': heal}
    return render(request, 'blog/health.html', context)


def politics(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    paginator = Paginator(poli, 10)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal, 'sports': sports, 'technology': technology}
    return render(request, 'blog/politics.html', context)


def sport(request):
    sports = News.objects.all().filter(category='sport')
    context = {'sports': sports}
    return render(request, 'blog/sport.html', context)


def tech(request):
    technology = News.objects.all().filter(category='tech')
    context = {'arts': technology}
    return render(request, 'blog/tech.html', context)


def contact(request):
    return render(request, 'blog/contact.html')

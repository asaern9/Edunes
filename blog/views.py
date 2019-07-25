from django.shortcuts import render, reverse
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        context['related_post_arts'] = News.objects.filter(category='arts').order_by('-id')[:4]
        return context


def arts_culture(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    page = request.GET.get('page', 1)
    paginator = Paginator(arts, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news}
    return render(request, 'blog/arts_culture.html', context)


def business(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    page = request.GET.get('page', 1)
    paginator = Paginator(bus, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news}
    return render(request, 'blog/business.html', context)


def entertainment(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    page = request.GET.get('page', 1)
    paginator = Paginator(enter, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news}
    return render(request, 'blog/entertainment.html', context)


def fashion(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    page = request.GET.get('page', 1)
    paginator = Paginator(fash, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news}
    return render(request, 'blog/fashion.html', context)


def health(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    page = request.GET.get('page', 1)
    paginator = Paginator(heal, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash,
               'sports': sports, 'technology': technology, 'news': news}
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

    page = request.GET.get('page', 1)
    paginator = Paginator(poli, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news}
    return render(request, 'blog/politics.html', context)


def sport(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]

    page = request.GET.get('page', 1)
    paginator = Paginator(sports, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'technology': technology, 'news': news}
    return render(request, 'blog/sport.html', context)


def tech(request):
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(technology, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'news': news}
    return render(request, 'blog/tech.html', context)


def contact(request):
    return render(request, 'blog/contact.html')

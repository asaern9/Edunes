from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News, FeaturedVideo
from .forms import ContactForm, PublishForm
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    news = News.objects.all().order_by('-id')[:6]
    arts = News.objects.all().filter(category='arts').order_by('-id')[:1]
    bus = News.objects.all().filter(category='business').order_by('-id')[:1]
    bus_2 = News.objects.all().filter(category='business').order_by('-id')
    enter = News.objects.all().filter(category='entertainment').order_by('-id')[:1]
    enter_2 = News.objects.all().filter(category='entertainment').order_by('-id')
    fash = News.objects.all().filter(category='fashion').order_by('-id')[:1]
    heal = News.objects.all().filter(category='health').order_by('-id')[:1]
    poli = News.objects.all().filter(category='politics').order_by('-id')[:1]
    poli_2 = News.objects.all().filter(category='politics')[:2]
    sports = News.objects.all().filter(category='sport').order_by('-id')[:1]
    technology = News.objects.all().filter(category='tech').order_by('-id')[:1]
    technology_2 = News.objects.all().filter(category='tech').order_by('-id')
    video_link = FeaturedVideo.objects.all().order_by('-id')[:3]
    context = {'news': news, 'arts': arts, 'politics': poli, 'business': bus, 'entertainment': enter, 'fashion': fash,
               'health': heal, 'sports': sports, 'technology': technology, 'politics_2': poli_2, 'enter_2': enter_2,
               'technology_2': technology_2, 'bus_2': bus_2, 'video_link': video_link}
    return render(request, 'blog/index.html', context)


class NewsDetail(DetailView):
    model = News
    template_name = 'blog/news_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsDetail, self).get_context_data(*args, **kwargs)
        context['politics_related'] = News.objects.filter(category='politics').order_by('-id')[:4]
        context['arts_related'] = News.objects.filter(category='arts').order_by('-id')[:4]
        context['tech_related'] = News.objects.filter(category='tech').order_by('-id')[:4]
        context['fashion_related'] = News.objects.filter(category='fashion').order_by('-id')[:4]
        context['entertainment_related'] = News.objects.filter(category='entertainment').order_by('-id')[:4]
        context['health_related'] = News.objects.filter(category='health').order_by('-id')[:4]
        context['sport_related'] = News.objects.filter(category='sport').order_by('-id')[:4]
        context['business_related'] = News.objects.filter(category='business').order_by('-id')[:4]
        context['latest_news'] = News.objects.all().order_by('-id')[:4]
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(arts, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(bus, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(enter, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(fash, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(heal, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash,
               'sports': sports, 'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(poli, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(sports, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'technology': technology, 'news': news, 'popular': popular}
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
    popular = News.objects.all().filter(most_popular=True).order_by('-id')[:4]
    page = request.GET.get('page', 1)
    paginator = Paginator(technology, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {'politics': poli, 'arts': arts, 'business': bus, 'entertainment': enter, 'fashion': fash, 'health': heal,
               'sports': sports, 'news': news, 'popular': popular}
    return render(request, 'blog/tech.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            messages.success(request, 'Message submitted!')
            send_mail(
                'Contact Message received',
                'Checkout the message on the admin panel Now!',
                'info.edunes@gmail.com',
                ['asaern9@gmail.com'],
                fail_silently=False,
            )
            return redirect('blog-contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html')


class SearchResultsView(ListView):
    model = News
    template_name = 'blog/search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = News.objects.filter(title__icontains=query).union(News.objects.filter(content__icontains=query))
            return object_list


def publish(request):
    if request.method == 'POST':
        form = PublishForm(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save()
            messages.success(request, 'News submitted for approval')
            send_mail(
                'News publish request received',
                'Checkout the news request on the admin panel Now!',
                'info.edunes@gmail.com',
                ['asaern9@gmail.com'],
                fail_silently=False,
            )
            return redirect('blog-publish')
    else:
        form = PublishForm()
    return render(request, 'blog/publish.html', {'form': form})


# Universities views

def university_of_ghana(request):
    return render(request, 'blog/university_of_ghana.html')
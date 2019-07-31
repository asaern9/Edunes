from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import NewsDetail, SearchResultsView

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('search/', SearchResultsView.as_view(), name='search-result'),
    path('news/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('arts_culture/', views.arts_culture, name='blog-arts-culture'),
    path('business/', views.business, name='blog-business'),
    path('entertainment/', views.entertainment, name='blog-entertainment'),
    path('fashion/', views.fashion, name='blog-fashion'),
    path('health/', views.health, name='blog-health'),
    path('politics/', views.politics, name='blog-politics'),
    path('sports/', views.sport, name='blog-sport'),
    path('technology/', views.tech, name='blog-technology'),
    path('contact/', views.contact, name='blog-contact'),

    # Universities url path
    path('institutions/university-of-ghaan/', views.university_of_ghana, name='university-of-ghana'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import NewsDetail

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('news/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('arts_culture/', views.arts_culture, name='blog-arts-culture'),
    path('arts_culture/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('business/', views.business, name='blog-business'),
    path('business/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('entertainment/', views.entertainment, name='blog-entertainment'),
    path('entertainment/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('fashion/', views.fashion, name='blog-fashion'),
    path('fashion/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('health/', views.health, name='blog-health'),
    path('health/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('politics/', views.politics, name='blog-politics'),
    path('politics/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('sports/', views.sport, name='blog-sport'),
    path('sports/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('technology/', views.tech, name='blog-technology'),
    path('technology/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),

    path('contact/', views.contact, name='blog-contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

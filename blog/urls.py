from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import NewsDetail

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('news/<slug>/', NewsDetail.as_view(), name='blog-news-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.db import models
from django.shortcuts import reverse
# Create your models here.
CATEGORY_CHOICES = (
    ('arts', 'Arts/Culture'),
    ('business', 'Business'),
    ('entertainment', 'Entertainment'),
    ('fashion', 'Fashion'),
    ('health', 'Health'),
    ('politics', 'Politics'),
    ('sport', 'Sport'),
    ('tech', 'Tech'),
)


class News(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField()
    reporter = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    slug = models.SlugField(null=True)
    picture = models.ImageField(upload_to='News/')
    audio = models.FileField(upload_to='Audio/', null=True, blank=True)
    most_popular = models.BooleanField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog-news-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title + '---------' + self.category


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name + '--------' + self.subject


class FeaturedVideo(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    video_link = models.URLField(max_length=500)
    video_picture = models.ImageField(upload_to='Videos_Pic/')

    def __str__(self):
        return self.title


class UnapprovedNews(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    picture = models.ImageField(upload_to='Unapproved/', null=True)
    reporter = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Arts/Culture')
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    video = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

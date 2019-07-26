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

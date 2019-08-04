from django.contrib import admin
from .models import News, Message, FeaturedVideo, UnapprovedNews
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


class UnapprovedAdmin(admin.ModelAdmin):
    list_display = ('title', 'reporter')


admin.site.register(News, NewsAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(FeaturedVideo)
admin.site.register(UnapprovedNews, UnapprovedAdmin)

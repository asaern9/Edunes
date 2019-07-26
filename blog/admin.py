from django.contrib import admin
from .models import News, Message
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(News, NewsAdmin)
admin.site.register(Message, MessageAdmin)

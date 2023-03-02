from django.contrib import admin
from .models import ConversationItem, MessageItem

admin.site.register(ConversationItem)
admin.site.register(MessageItem)

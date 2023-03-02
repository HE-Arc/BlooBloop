from django.contrib import admin
from .models import ConversationItem, MessageItem, ProfileItem

admin.site.register(ConversationItem)
admin.site.register(MessageItem)
admin.site.register(ProfileItem)

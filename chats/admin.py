from django.contrib import admin
from .models import ChatGroup, GroupMessages

admin.site.register(GroupMessages)
admin.site.register(ChatGroup)
